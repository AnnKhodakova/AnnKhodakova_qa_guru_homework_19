from voluptuous import Schema, PREVENT_EXTRA

colors_schema = Schema({
    "id": int,
    "name": str,
    "year": int,
    "color": str,
    "pantone_value": str
}
    , extra=PREVENT_EXTRA,
    required=True)

list_shema = Schema(
    {
        "page": int,
        "per_page": int,
        "total": int,
        "total_pages": int,
        "data": [colors_schema],
        "support": {
            "url": str,
            "text": str
        }
    },
    extra=PREVENT_EXTRA,
    required=True
)
