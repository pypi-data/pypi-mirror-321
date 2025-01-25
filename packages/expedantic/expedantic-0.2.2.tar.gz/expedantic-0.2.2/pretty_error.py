from typing import Type, List, Dict, Any
from pydantic import BaseModel, ValidationError
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree
from rich.table import Table
from rich.text import Text
from rich import box
from itertools import groupby
from operator import itemgetter


def print_validation_errors(
    model_cls: Type[BaseModel],
    validation_error: ValidationError,
    field_infos: Dict[str, Any],
) -> None:
    """
    Pretty print Pydantic validation errors with field context.

    Args:
        model_cls: The Pydantic model class
        validation_error: The ValidationError exception
        field_infos: Dictionary of field information from get_field_info()
    """
    console = Console()
    errors = validation_error.errors()

    # Group errors by type
    errors_by_type = {
        k: list(g)
        for k, g in groupby(
            sorted(errors, key=itemgetter("type")), key=itemgetter("type")
        )
    }

    main_tree = Tree(f"[bold red]Validation Errors for {model_cls.__name__}")

    def get_field_context(loc: tuple) -> str:
        """Get field description and constraints for context."""
        field_path = ".".join(str(x) for x in loc)
        field_info = field_infos.get(field_path)
        if not field_info:
            return ""

        context = []
        if field_info.description:
            context.append(f"Description: {field_info.description}")

        # Add validation rules
        rules = []
        for rule in [
            "gt",
            "ge",
            "lt",
            "le",
            "min_length",
            "max_length",
            "regex",
            "pattern",
            "multiple_of",
        ]:
            value = getattr(field_info, rule, None)
            if value is not None:
                rules.append(f"{rule}: {value}")

        if rules:
            context.append("Validation rules: " + ", ".join(rules))

        return "\n".join(context)

    # Handle missing fields
    if "missing" in errors_by_type:
        missing_node = main_tree.add("[yellow]Missing Required Fields")
        missing_table = Table(box=box.ROUNDED, show_header=True)
        missing_table.add_column("Field", style="bold yellow")
        missing_table.add_column("Context", style="italic")

        for error in errors_by_type["missing"]:
            field_path = ".".join(str(x) for x in error["loc"])
            context = get_field_context(error["loc"])
            missing_table.add_row(field_path, context)

        missing_node.add(missing_table)

    # Handle type errors
    if "type_error" in errors_by_type:
        type_node = main_tree.add("[red]Type Errors")
        type_table = Table(box=box.ROUNDED, show_header=True)
        type_table.add_column("Field", style="bold red")
        type_table.add_column("Error", style="italic")
        type_table.add_column("Context", style="dim")

        for error in errors_by_type["type_error"]:
            field_path = ".".join(str(x) for x in error["loc"])
            context = get_field_context(error["loc"])
            type_table.add_row(field_path, error["msg"], context)

        type_node.add(type_table)

    # Handle value errors
    if "value_error" in errors_by_type:
        value_node = main_tree.add("[magenta]Value Errors")
        value_table = Table(box=box.ROUNDED, show_header=True)
        value_table.add_column("Field", style="bold magenta")
        value_table.add_column("Error", style="italic")
        value_table.add_column("Context", style="dim")

        for error in errors_by_type["value_error"]:
            field_path = ".".join(str(x) for x in error["loc"])
            context = get_field_context(error["loc"])
            value_table.add_row(field_path, error["msg"], context)

        value_node.add(value_table)

    # Handle other types of errors
    other_errors = {
        k: v
        for k, v in errors_by_type.items()
        if k not in ["missing", "type_error", "value_error"]
    }
    if other_errors:
        other_node = main_tree.add("[blue]Other Validation Errors")
        other_table = Table(box=box.ROUNDED, show_header=True)
        other_table.add_column("Type", style="bold blue")
        other_table.add_column("Field", style="bold")
        other_table.add_column("Error", style="italic")
        other_table.add_column("Context", style="dim")

        for error_type, errors in other_errors.items():
            for error in errors:
                field_path = ".".join(str(x) for x in error["loc"])
                context = get_field_context(error["loc"])
                other_table.add_row(error_type, field_path, error["msg"], context)

        other_node.add(other_table)

    # Print the error tree
    console.print(Panel(main_tree, title="Validation Errors", border_style="red"))


# Example usage
if __name__ == "__main__":
    from datetime import datetime
    from pydantic import Field, EmailStr
    from typing import Optional, List

    class Address(BaseModel):
        street: str = Field(..., min_length=5, description="Street address")
        city: str = Field(..., pattern="^[A-Za-z ]+$", description="City name")
        postal_code: str = Field(
            ..., pattern=r"^\d{5}$", description="5-digit postal code"
        )

    class User(BaseModel):
        name: str = Field(..., min_length=2, description="User's full name")
        age: int = Field(..., ge=0, le=150, description="User's age in years")
        email: EmailStr = Field(..., description="Valid email address")
        address: Address = Field(..., description="User's primary address")
        tags: Optional[List[str]] = Field(
            None, min_length=1, description="Optional user tags"
        )

    # Test with invalid data
    try:
        user = User.model_validate(
            {
                "name": "A",  # too short
                "age": -1,  # negative age
                "email": "not_an_email",  # invalid email
                "address": {
                    "street": "123",  # too short
                    "city": "New York123",  # contains numbers
                    "postal_code": "1234",  # not 5 digits
                },
                "tags": [],  # empty list
            }
        )
    except ValidationError as e:
        # Get field info using the previously defined get_field_info function
        from expedantic.utils import get_field_info

        field_infos = get_field_info(User)

        # Print validation errors with context
        print_validation_errors(User, e, field_infos)

    from enum import Enum
    from typing import List, Optional, Dict, Any
    from datetime import datetime, date
    from pydantic import BaseModel, Field, EmailStr, HttpUrl, constr

    class PaymentType(str, Enum):
        CREDIT = "credit"
        DEBIT = "debit"
        CRYPTO = "crypto"

    class CardInfo(BaseModel):
        card_number: str = Field(
            ..., pattern=r"^\d{16}$", description="16-digit card number"
        )
        expiry_date: date = Field(..., description="Card expiry date")
        cvv: str = Field(
            ..., pattern=r"^\d{3,4}$", description="3 or 4 digit security code"
        )
        billing_zip: str = Field(
            ..., pattern=r"^\d{5}$", description="5-digit billing ZIP code"
        )

    class PaymentMethod(BaseModel):
        type: PaymentType = Field(..., description="Type of payment method")
        is_default: bool = Field(
            False, description="Whether this is the default payment method"
        )
        card_info: Optional[CardInfo] = Field(
            None, description="Credit/debit card information"
        )
        nickname: Optional[str] = Field(
            None,
            min_length=2,
            max_length=50,
            description="User-defined name for this payment method",
        )

    class ContactPreferences(BaseModel):
        email_marketing: bool = Field(False, description="Accept marketing emails")
        sms_updates: bool = Field(False, description="Accept SMS updates")
        push_notifications: bool = Field(False, description="Accept push notifications")
        frequency: str = Field(
            "daily",
            pattern="^(daily|weekly|monthly)$",
            description="Contact frequency preference",
        )

    class SocialMedia(BaseModel):
        platform: str = Field(
            ...,
            pattern="^(twitter|facebook|instagram|linkedin)$",
            description="Social media platform name",
        )
        username: str = Field(
            ..., min_length=2, max_length=50, description="Username on the platform"
        )
        profile_url: HttpUrl = Field(
            ..., description="Full URL to social media profile"
        )
        followers_count: Optional[int] = Field(
            None, ge=0, description="Number of followers"
        )

    class Location(BaseModel):
        latitude: float = Field(..., ge=-90, le=90, description="Latitude coordinate")
        longitude: float = Field(
            ..., ge=-180, le=180, description="Longitude coordinate"
        )
        accuracy: float = Field(..., gt=0, le=100, description="Accuracy in meters")

    class Address(BaseModel):
        street_line1: str = Field(
            ..., min_length=5, max_length=100, description="Primary street address"
        )
        street_line2: Optional[str] = Field(
            None, max_length=100, description="Secondary street address"
        )
        city: str = Field(..., pattern="^[A-Za-z ]+$", description="City name")
        state: str = Field(
            ..., pattern="^[A-Z]{2}$", description="Two-letter state code"
        )
        postal_code: str = Field(
            ..., pattern=r"^\d{5}(-\d{4})?$", description="ZIP code with optional +4"
        )
        country: str = Field(
            "US", pattern="^[A-Z]{2}$", description="Two-letter country code"
        )
        location: Optional[Location] = Field(None, description="Geographic coordinates")
        is_primary: bool = Field(
            True, description="Whether this is the primary address"
        )

    class Profile(BaseModel):
        bio: Optional[str] = Field(None, max_length=500, description="User biography")
        birth_date: date = Field(..., description="User's date of birth")
        avatar_url: Optional[HttpUrl] = Field(
            None, description="URL to user's avatar image"
        )
        social_media: List[SocialMedia] = Field(
            default_factory=list,
            max_length=5,
            description="Connected social media accounts",
        )
        preferences: ContactPreferences = Field(
            ..., description="User contact preferences"
        )
        languages: List[str] = Field(
            ..., min_length=1, description="List of spoken languages"
        )

    class User(BaseModel):
        id: int = Field(..., gt=0, description="Unique user identifier")
        username: str = Field(
            ...,
            min_length=3,
            max_length=50,
            pattern="^[a-zA-Z0-9_-]+$",
            description="Unique username",
        )
        email: EmailStr = Field(..., description="Primary email address")
        full_name: str = Field(
            ..., min_length=2, max_length=100, description="User's full name"
        )
        phone: str = Field(
            ...,
            pattern=r"^\+\d{1,3}-\d{3}-\d{3}-\d{4}$",
            description="Phone number in international format",
        )
        profile: Profile = Field(..., description="User profile information")
        addresses: List[Address] = Field(
            ..., min_length=1, description="User's addresses"
        )
        payment_methods: List[PaymentMethod] = Field(
            default_factory=list,
            max_length=5,
            description="User's saved payment methods",
        )
        settings: Dict[str, Any] = Field(
            default_factory=dict, description="User preferences and settings"
        )
        created_at: datetime = Field(
            default_factory=datetime.now, description="Account creation timestamp"
        )
        last_login: Optional[datetime] = Field(None, description="Last login timestamp")

    # Example invalid data
    invalid_data = {
        "id": -1,  # Invalid: must be positive
        "username": "user@123",  # Invalid: contains @
        "email": "not-an-email",  # Invalid: not a valid email
        "full_name": "J",  # Invalid: too short
        "phone": "123-456-7890",  # Invalid: wrong format
        "profile": {
            "birth_date": "2025-01-01",  # Invalid: future date
            "languages": [],  # Invalid: empty list
            "social_media": [
                {
                    "platform": "myspace",  # Invalid: not in allowed platforms
                    "username": "u",  # Invalid: too short
                    "profile_url": "not-a-url",  # Invalid: not a valid URL
                    "followers_count": -100,  # Invalid: negative number
                }
            ],
            "preferences": {"frequency": "hourly"},  # Invalid: not in allowed values
        },
        "addresses": [
            {
                "street_line1": "123",  # Invalid: too short
                "city": "New York123",  # Invalid: contains numbers
                "state": "NYC",  # Invalid: not 2 letters
                "postal_code": "1234",  # Invalid: wrong format
                "location": {
                    "latitude": 100,  # Invalid: > 90
                    "longitude": 200,  # Invalid: > 180
                    "accuracy": 0,  # Invalid: must be > 0
                },
            }
        ],
        "payment_methods": [
            {
                "type": "bitcoin",  # Invalid: not in PaymentType
                "card_info": {
                    "card_number": "123",  # Invalid: not 16 digits
                    "expiry_date": "2020-01-01",  # Invalid: past date
                    "cvv": "12345",  # Invalid: too many digits
                    "billing_zip": "1234",  # Invalid: not 5 digits
                },
            }
        ],
    }

    try:
        user = User.model_validate(invalid_data)
    except ValidationError as e:
        # field_infos = get_field_info(User)
        # print_validation_errors(User, e, field_infos)
        from expedantic.printers import print_validation_errors

        print_validation_errors(User, e)
