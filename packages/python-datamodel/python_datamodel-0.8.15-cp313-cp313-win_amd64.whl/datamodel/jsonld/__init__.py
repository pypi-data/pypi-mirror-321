from .models import (
    URL,
    JobTitle,
    PostalAddress,
    GeoCoordinates,
    Person,
    ImageObject,
    Recipe,
    NutritionInformation,
    Organization,
    AggregateRating,
    Rating,
    Product,
    Review,
    VideoObject,
    AdministrativeArea,
    Audience,
    Place,
    QuantitativeValue,
    MonetaryAmount,
    JobPosting,
)

JSON_MODEL_MAP = {
    "URL": URL,
    "JobTitle": JobTitle,
    "PostalAddress": PostalAddress,
    "GeoCoordinates": GeoCoordinates,
    "Person": Person,
    "ImageObject": ImageObject,
    "Recipe": Recipe,
    "NutritionInformation": NutritionInformation,
    "Organization": Organization,
    "AggregateRating": AggregateRating,
    "Rating": Rating,
    "Product": Product,
    "Review": Review,
    "VideoObject": VideoObject,
    "AdministrativeArea": AdministrativeArea,
    "Audience": Audience,
    "Place": Place,
    "QuantitativeValue": QuantitativeValue,
    "MonetaryAmount": MonetaryAmount,
    "JobPosting": JobPosting,
}
