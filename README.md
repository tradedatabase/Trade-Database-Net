# Global Trade Data Toolkit 🌍📦

Open, free reference datasets and a tiny Python toolkit for working with
**international trade data** — bill of lading (shipment) records, customs
declarations, HS codes, and country-level import/export summaries.

If you've ever needed to answer *"who imports this product, from where, and in
what volume?"* — this repo is a practical starting point, with real
aggregate numbers and a clear map of what full shipment data contains.

---

## What's inside

| File | What it is |
|------|------------|
| [`data/country-trade-summary.csv`](data/country-trade-summary.csv) | Aggregate **import/export shipment counts** for **184 countries**, plus each country's top trading partner and top traded commodity. Aggregate only — no company data. |
| [`data/hs-code-commodity-reference.csv`](data/hs-code-commodity-reference.csv) | A quick **HS-code ↔ commodity** reference across 80 major traded goods. |
| [`data/bill-of-lading-data-dictionary.csv`](data/bill-of-lading-data-dictionary.csv) | The **67 fields** in a full bill-of-lading shipment record, each explained in plain terms. |
| [`toolkit/analyze.py`](toolkit/analyze.py) | Zero-dependency Python to explore the data (top importers/exporters, per-country summary). |

## Quick start

```bash
python toolkit/analyze.py            # top importing & exporting countries
python toolkit/analyze.py China      # summary for a single country
python toolkit/analyze.py --commodities
```

Example output:

```
China — trade summary
  Import shipments : 1,616,259,915
  Export shipments : 1,775,241,465
  Top import source: Hong Kong (21%)
  Top export market: United States (28%)
  Top export good  : Electronics
```

---

## What is trade data?

**Bill of lading data** is built from ocean shipment manifests. Each record ties
a product (by HS code) to the exporter (shipper) and importer (consignee), the
countries and ports involved, the vessel and container, and the weight/volume —
so you can find real suppliers and buyers for any product.

**Customs data** comes from customs declarations and adds tax IDs, customs value,
duty and CIF/FOB terms — useful for benchmarking landed cost.

The [data dictionary](data/bill-of-lading-data-dictionary.csv) lists every field
in a full record. The company-level fields (importer/exporter name, address,
phone, email) are what turn aggregate trends into an actionable contact list.

## Full, company-level datasets

The samples here are **aggregate** (no company details). Full bill-of-lading and
customs datasets — with the actual importers & exporters, contacts, HS codes and
volumes for **195+ countries, 2015–2026** — are available at
**[tradedatabase.net](https://tradedatabase.net)**:

- [China Bill of Lading data](https://tradedatabase.net/dataset/china-bill-of-lading-data-export-import-2015-2026)
- [China Customs data](https://tradedatabase.net/dataset/china-customs-data-2015-2026)
- [Browse all countries](https://tradedatabase.net/countries) · [Free sample](https://tradedatabase.net/sample)

## License

- **Data** (`/data`): [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — free to use with attribution to [tradedatabase.net](https://tradedatabase.net).
- **Code** (`/toolkit`): MIT.

## Contributing

Issues and PRs welcome — corrections to the reference data, new analysis
helpers, or additional aggregate slices.
