# drugbank_schemas (v0.1.0)

<p align="center">
    <img src="https://img.shields.io/pypi/dm/rxiv-types?style=flat-square" />
    <img src="https://img.shields.io/pypi/l/rxiv-types?style=flat-square"/>
    <img src="https://img.shields.io/pypi/v/rxiv-types?style=flat-square"/>
    <a href="https://github.com/tefra/xsdata-pydantic">
        <img alt="Built with: xsdata-pydantic" src="https://img.shields.io/badge/Built%20with-xsdata--pydantic-blue">
    </a>
    <a href="https://github.com/dbrgn/coverage-badge">
        <img src="./images/coverage.svg">
    </a>
</p>

## Introduction

The purpose of this package is to provide Pydantic models for Drugbank schema files (XSD). 
It generates Pydantic classes that help parse Drugbank XML Data files.
`xsdata-pydantic` tool. 

## How to install it?
pip install drugbank-schemas

## How do I use it?
You can import the generated Pydantic models for drunbank schema files and use them 
to parse your drugbank XML files.

```python
from xsdata_pydantic.bindings import XmlParser
from xsdata.formats.dataclass.context import XmlContext

from drugbank_schemas.models.drugbank_latest import Drugbank

parser = XmlParser(context=XmlContext())
drugbank = parser.parse("drugbank_5.1.10.xml", Drugbank)
```
