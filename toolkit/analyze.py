#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tiny, dependency-free toolkit for the open trade-data samples in this repo.

Usage:
    python toolkit/analyze.py                # top importers & exporters
    python toolkit/analyze.py China          # summary for one country
    python toolkit/analyze.py --commodities  # HS-code / commodity reference

Data: ../data/country-trade-summary.csv  (aggregate shipment counts, no PII)
"""
import csv, os, sys

HERE = os.path.dirname(__file__)
DATA = os.path.join(HERE, "..", "data")


def load(name):
    with open(os.path.join(DATA, name), encoding="utf-8") as f:
        return list(csv.DictReader(f))


def num(x):
    try:
        return int(x)
    except (TypeError, ValueError):
        return 0


def top(rows, key, n=10):
    return sorted(rows, key=lambda r: num(r[key]), reverse=True)[:n]


def country(rows, name):
    for r in rows:
        if r["country"].lower() == name.lower():
            print(f"\n{r['country']} — trade summary")
            print(f"  Import shipments : {num(r['import_shipments']):,}")
            print(f"  Export shipments : {num(r['export_shipments']):,}")
            print(f"  Top import source: {r['top_import_source']} ({r['import_source_share_pct']}%)")
            print(f"  Top export market: {r['top_export_market']} ({r['export_market_share_pct']}%)")
            print(f"  Top export good  : {r['top_export_commodity']}")
            print(f"  Top import good  : {r['top_import_commodity']}")
            return
    print(f"Country '{name}' not found.")


def main():
    rows = load("country-trade-summary.csv")
    if len(sys.argv) > 1 and sys.argv[1] == "--commodities":
        for r in load("hs-code-commodity-reference.csv"):
            print(f"{r['commodity']:<28} HS {r['hs_code_prefixes']}")
        return
    if len(sys.argv) > 1:
        country(rows, " ".join(sys.argv[1:]))
        return
    print("Top 10 importing countries (by recorded shipments)")
    for r in top(rows, "import_shipments"):
        print(f"  {r['country']:<24} {num(r['import_shipments']):>15,}")
    print("\nTop 10 exporting countries (by recorded shipments)")
    for r in top(rows, "export_shipments"):
        print(f"  {r['country']:<24} {num(r['export_shipments']):>15,}")
    print("\nFull dataset (company-level bill of lading & customs records) at https://tradedatabase.net")


if __name__ == "__main__":
    main()
