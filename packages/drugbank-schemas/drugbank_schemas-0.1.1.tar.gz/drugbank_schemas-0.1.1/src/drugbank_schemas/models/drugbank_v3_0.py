from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Union

__NAMESPACE__ = "http://drugbank.ca"


@dataclass
class BondActionsType:
    action: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
        },
    )


class DrugTypeType(Enum):
    SMALL_MOLECULE = "small molecule"
    BIOTECH = "biotech"


class EmptyStringType(Enum):
    VALUE = ""


@dataclass
class IdentifiersType:
    external_identifier: List["IdentifiersType.ExternalIdentifier"] = field(
        default_factory=list,
        metadata={
            "name": "external-identifier",
            "type": "Element",
            "namespace": "http://drugbank.ca",
        },
    )

    @dataclass
    class ExternalIdentifier:
        resource: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://drugbank.ca",
                "required": True,
            },
        )
        identifier: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://drugbank.ca",
                "required": True,
            },
        )


class PropertyTypeKind(Enum):
    LOG_P = "logP"
    LOG_S = "logS"
    LOG_P_HYDROPHOBICITY = "logP/hydrophobicity"
    WATER_SOLUBILITY = "Water Solubility"
    CACO2_PERMEABILITY = "caco2 Permeability"
    P_KA_STRONGEST_ACIDIC = "pKa (strongest acidic)"
    P_KA_STRONGEST_BASIC = "pKa (strongest basic)"
    IUPAC_NAME = "IUPAC Name"
    MOLECULAR_WEIGHT = "Molecular Weight"
    MONOISOTOPIC_WEIGHT = "Monoisotopic Weight"
    SMILES = "SMILES"
    MOLECULAR_FORMULA = "Molecular Formula"
    IN_CH_I = "InChI"
    IN_CH_IKEY = "InChIKey"
    POLAR_SURFACE_AREA_PSA = "Polar Surface Area (PSA)"
    REFRACTIVITY = "Refractivity"
    POLARIZABILITY = "Polarizability"
    ROTATABLE_BOND_COUNT = "Rotatable Bond Count"
    H_BOND_ACCEPTOR_COUNT = "H Bond Acceptor Count"
    H_BOND_DONOR_COUNT = "H Bond Donor Count"
    PHYSIOLOGICAL_CHARGE = "Physiological Charge"


class PropertyTypeSource(Enum):
    JCHEM = "JChem"
    ALOGPS = "ALOGPS"
    VALUE = ""


@dataclass
class SequenceType:
    header: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    chain: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )


@dataclass
class SynonymsType:
    synonym: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
        },
    )


class TargetBondTypeKnownAction(Enum):
    YES = "yes"
    NO = "no"
    UNKNOWN = "unknown"


@dataclass
class AffectedOrganisms:
    class Meta:
        name = "affected-organisms"
        namespace = "http://drugbank.ca"

    affected_organism: List[str] = field(
        default_factory=list,
        metadata={
            "name": "affected-organism",
            "type": "Element",
        },
    )


@dataclass
class AhfsCodes:
    class Meta:
        name = "ahfs-codes"
        namespace = "http://drugbank.ca"

    ahfs_code: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ahfs-code",
            "type": "Element",
        },
    )


@dataclass
class AtcCodes:
    class Meta:
        name = "atc-codes"
        namespace = "http://drugbank.ca"

    atc_code: List[str] = field(
        default_factory=list,
        metadata={
            "name": "atc-code",
            "type": "Element",
        },
    )


@dataclass
class Brands:
    class Meta:
        name = "brands"
        namespace = "http://drugbank.ca"

    brand: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Categories:
    class Meta:
        name = "categories"
        namespace = "http://drugbank.ca"

    category: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Cost:
    class Meta:
        name = "cost"
        namespace = "http://drugbank.ca"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    currency: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Dosage:
    class Meta:
        name = "dosage"
        namespace = "http://drugbank.ca"

    form: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    route: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    strength: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class DrugInteraction:
    class Meta:
        name = "drug-interaction"
        namespace = "http://drugbank.ca"

    drug: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


class EssentialityValue(Enum):
    ESSENTIAL = "Essential"
    NON_ESSENTIAL = "Non-Essential"


@dataclass
class ExternalLink:
    class Meta:
        name = "external-link"
        namespace = "http://drugbank.ca"

    resource: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class FoodInteractions:
    class Meta:
        name = "food-interactions"
        namespace = "http://drugbank.ca"

    food_interaction: List[str] = field(
        default_factory=list,
        metadata={
            "name": "food-interaction",
            "type": "Element",
        },
    )


@dataclass
class GoClassifier:
    class Meta:
        name = "go-classifier"
        namespace = "http://drugbank.ca"

    category: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


class GroupsGroup(Enum):
    APPROVED = "approved"
    ILLICIT = "illicit"
    EXPERIMENTAL = "experimental"
    WITHDRAWN = "withdrawn"
    NUTRACEUTICAL = "nutraceutical"


@dataclass
class Manufacturer:
    class Meta:
        name = "manufacturer"
        namespace = "http://drugbank.ca"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    generic: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Mixture:
    class Meta:
        name = "mixture"
        namespace = "http://drugbank.ca"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    ingredients: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Packager:
    class Meta:
        name = "packager"
        namespace = "http://drugbank.ca"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Patent:
    class Meta:
        name = "patent"
        namespace = "http://drugbank.ca"

    number: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    country: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    approved: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    expires: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Pfam:
    class Meta:
        name = "pfam"
        namespace = "http://drugbank.ca"

    identifier: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Salts:
    class Meta:
        name = "salts"
        namespace = "http://drugbank.ca"

    salt: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class SecondaryAccessionNumbers:
    class Meta:
        name = "secondary-accession-numbers"
        namespace = "http://drugbank.ca"

    secondary_accession_number: List[str] = field(
        default_factory=list,
        metadata={
            "name": "secondary-accession-number",
            "type": "Element",
        },
    )


class SpeciesCategory(Enum):
    HUMAN = "human"
    BACTERIAL = "bacterial"
    FUNGAL = "fungal"
    VIRAL = "viral"
    PARASITIC = "parasitic"


@dataclass
class Substructure:
    class Meta:
        name = "substructure"
        namespace = "http://drugbank.ca"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class BondType:
    actions: Optional[BondActionsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    references: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    position: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    partner: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class PropertyType:
    kind: Optional[PropertyTypeKind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    source: Optional[PropertyTypeSource] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )


@dataclass
class Dosages:
    class Meta:
        name = "dosages"
        namespace = "http://drugbank.ca"

    dosage: List[Dosage] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class DrugInteractions:
    class Meta:
        name = "drug-interactions"
        namespace = "http://drugbank.ca"

    drug_interaction: List[DrugInteraction] = field(
        default_factory=list,
        metadata={
            "name": "drug-interaction",
            "type": "Element",
        },
    )


@dataclass
class Essentiality:
    class Meta:
        name = "essentiality"
        namespace = "http://drugbank.ca"

    value: Optional[EssentialityValue] = field(default=None)


@dataclass
class ExternalLinks:
    class Meta:
        name = "external-links"
        namespace = "http://drugbank.ca"

    external_link: List[ExternalLink] = field(
        default_factory=list,
        metadata={
            "name": "external-link",
            "type": "Element",
        },
    )


@dataclass
class GoClassifiers:
    class Meta:
        name = "go-classifiers"
        namespace = "http://drugbank.ca"

    go_classifier: List[GoClassifier] = field(
        default_factory=list,
        metadata={
            "name": "go-classifier",
            "type": "Element",
        },
    )


@dataclass
class Groups:
    class Meta:
        name = "groups"
        namespace = "http://drugbank.ca"

    group: List[GroupsGroup] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Manufacturers:
    class Meta:
        name = "manufacturers"
        namespace = "http://drugbank.ca"

    manufacturer: List[Manufacturer] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Mixtures:
    class Meta:
        name = "mixtures"
        namespace = "http://drugbank.ca"

    mixture: List[Mixture] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Packagers:
    class Meta:
        name = "packagers"
        namespace = "http://drugbank.ca"

    packager: List[Packager] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Patents:
    class Meta:
        name = "patents"
        namespace = "http://drugbank.ca"

    patent: List[Patent] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Pfams:
    class Meta:
        name = "pfams"
        namespace = "http://drugbank.ca"

    pfam: List[Pfam] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Price:
    class Meta:
        name = "price"
        namespace = "http://drugbank.ca"

    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    cost: Optional[Cost] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    unit: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ProteinSequences:
    class Meta:
        name = "protein-sequences"
        namespace = "http://drugbank.ca"

    protein_sequence: List[SequenceType] = field(
        default_factory=list,
        metadata={
            "name": "protein-sequence",
            "type": "Element",
        },
    )


@dataclass
class Species:
    class Meta:
        name = "species"
        namespace = "http://drugbank.ca"

    category: Optional[SpeciesCategory] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    uniprot_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "uniprot-name",
            "type": "Element",
        },
    )
    uniprot_taxon_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "uniprot-taxon-id",
            "type": "Element",
        },
    )


@dataclass
class Substructures:
    class Meta:
        name = "substructures"
        namespace = "http://drugbank.ca"

    substructure: List[Substructure] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class PartnerType:
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    general_function: Optional[str] = field(
        default=None,
        metadata={
            "name": "general-function",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    specific_function: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-function",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    gene_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "gene-name",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    locus: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    reaction: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    signals: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    cellular_location: Optional[str] = field(
        default=None,
        metadata={
            "name": "cellular-location",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    transmembrane_regions: Optional[str] = field(
        default=None,
        metadata={
            "name": "transmembrane-regions",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    theoretical_pi: Optional[Union[Decimal, EmptyStringType]] = field(
        default=None,
        metadata={
            "name": "theoretical-pi",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    molecular_weight: Optional[str] = field(
        default=None,
        metadata={
            "name": "molecular-weight",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    chromosome: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    species: Optional[Species] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    essentiality: Optional[Essentiality] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    references: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    external_identifiers: Optional[IdentifiersType] = field(
        default=None,
        metadata={
            "name": "external-identifiers",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    synonyms: Optional[SynonymsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    protein_sequence: Optional[SequenceType] = field(
        default=None,
        metadata={
            "name": "protein-sequence",
            "type": "Element",
            "namespace": "http://drugbank.ca",
        },
    )
    gene_sequence: Optional[SequenceType] = field(
        default=None,
        metadata={
            "name": "gene-sequence",
            "type": "Element",
            "namespace": "http://drugbank.ca",
        },
    )
    pfams: Optional[Pfams] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    go_classifiers: Optional[GoClassifiers] = field(
        default=None,
        metadata={
            "name": "go-classifiers",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class PropertiesType:
    property: List[PropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
        },
    )


@dataclass
class TargetBondType(BondType):
    known_action: Optional[TargetBondTypeKnownAction] = field(
        default=None,
        metadata={
            "name": "known-action",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )


@dataclass
class Carriers:
    class Meta:
        name = "carriers"
        namespace = "http://drugbank.ca"

    carrier: List[BondType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Enzymes:
    class Meta:
        name = "enzymes"
        namespace = "http://drugbank.ca"

    enzyme: List[BondType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Prices:
    class Meta:
        name = "prices"
        namespace = "http://drugbank.ca"

    price: List[Price] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Taxonomy:
    class Meta:
        name = "taxonomy"
        namespace = "http://drugbank.ca"

    kingdom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    substructures: Optional[Substructures] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Transporters:
    class Meta:
        name = "transporters"
        namespace = "http://drugbank.ca"

    transporter: List[BondType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Targets:
    class Meta:
        name = "targets"
        namespace = "http://drugbank.ca"

    target: List[TargetBondType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class DrugType:
    drugbank_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "drugbank-id",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    cas_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "cas-number",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    general_references: Optional[str] = field(
        default=None,
        metadata={
            "name": "general-references",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    synthesis_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "synthesis-reference",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    indication: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    pharmacology: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    mechanism_of_action: Optional[str] = field(
        default=None,
        metadata={
            "name": "mechanism-of-action",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    toxicity: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    biotransformation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    absorption: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    half_life: Optional[str] = field(
        default=None,
        metadata={
            "name": "half-life",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    protein_binding: Optional[str] = field(
        default=None,
        metadata={
            "name": "protein-binding",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    route_of_elimination: Optional[str] = field(
        default=None,
        metadata={
            "name": "route-of-elimination",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    volume_of_distribution: Optional[str] = field(
        default=None,
        metadata={
            "name": "volume-of-distribution",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    clearance: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    secondary_accession_numbers: Optional[SecondaryAccessionNumbers] = field(
        default=None,
        metadata={
            "name": "secondary-accession-numbers",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    groups: Optional[Groups] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    taxonomy: Optional[Taxonomy] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    synonyms: Optional[SynonymsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    salts: Optional[Salts] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    brands: Optional[Brands] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    mixtures: Optional[Mixtures] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    packagers: Optional[Packagers] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    manufacturers: Optional[Manufacturers] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    prices: Optional[Prices] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    categories: Optional[Categories] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    affected_organisms: Optional[AffectedOrganisms] = field(
        default=None,
        metadata={
            "name": "affected-organisms",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    dosages: Optional[Dosages] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    atc_codes: Optional[AtcCodes] = field(
        default=None,
        metadata={
            "name": "atc-codes",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    ahfs_codes: Optional[AhfsCodes] = field(
        default=None,
        metadata={
            "name": "ahfs-codes",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    patents: Optional[Patents] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    food_interactions: Optional[FoodInteractions] = field(
        default=None,
        metadata={
            "name": "food-interactions",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    drug_interactions: Optional[DrugInteractions] = field(
        default=None,
        metadata={
            "name": "drug-interactions",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    protein_sequences: Optional[ProteinSequences] = field(
        default=None,
        metadata={
            "name": "protein-sequences",
            "type": "Element",
            "namespace": "http://drugbank.ca",
        },
    )
    calculated_properties: Optional[PropertiesType] = field(
        default=None,
        metadata={
            "name": "calculated-properties",
            "type": "Element",
            "namespace": "http://drugbank.ca",
        },
    )
    experimental_properties: Optional[PropertiesType] = field(
        default=None,
        metadata={
            "name": "experimental-properties",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    external_identifiers: Optional[IdentifiersType] = field(
        default=None,
        metadata={
            "name": "external-identifiers",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    external_links: Optional[ExternalLinks] = field(
        default=None,
        metadata={
            "name": "external-links",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    targets: Optional[Targets] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    enzymes: Optional[Enzymes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    transporters: Optional[Transporters] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    carriers: Optional[Carriers] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        },
    )
    type_value: Optional[DrugTypeType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        },
    )
    updated: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    created: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Drugs:
    class Meta:
        name = "drugs"
        namespace = "http://drugbank.ca"

    drug: List[DrugType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    partners: Optional["Drugs.Partners"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    schema_version: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "schemaVersion",
            "type": "Attribute",
            "required": True,
        },
    )

    @dataclass
    class Partners:
        partner: List[PartnerType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )
