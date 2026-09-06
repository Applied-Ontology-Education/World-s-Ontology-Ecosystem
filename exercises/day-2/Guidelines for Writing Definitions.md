# **Guidelines for writing definitions in ontologies** 

### **Selja Seppälä** 

Ph.D., University of Geneva, Switzerland Postdoctoral Associate, University of Florida, Gainesville, United States. http://seljaseppala.wordpress.com _E-mail_ : sseppala@ufl.edu 

### **Alan Ruttenberg** 

M.S. Massachusetts Institute of Technology Director of Clinical Data Exchange, School of Dental Medicine, University at Buffalo, United States. http://alan.ruttenbergs.com _E-mail_ : alanruttenberg@gmail.com 

### **Barry Smith** 

Ph.D., University of Manchester, United Kingdom. Professor of Philosophy, University at Buffalo, Buffalo, United States. http://ontology.buffalo.edu/smith/ _E-mail_ : phismith@buffalo.edu 

Submetido em: 10/07/2017. Aprovado em: 05/09/2017. Publicado em: 28/12/2017. _Ciência da Informação_ 46 (1): 73-88 (2017) 

#### **ABSTRACT** 

Ontologies are being used increasingly to promote the reusability of scientific information by allowing heterogeneous data to be integrated under a common, normalized representation. Definitions play a central role in the use of ontologies both by humans and by computers. Textual definitions allow ontologists and data curators to understand the intended meaning of ontology terms and to use these terms in a consistent fashion across contexts. Logical definitions allow machines to check the integrity of ontologies and reason over data annotated with ontology terms to make inferences that promote knowledge discovery. Therefore, it is important not only to include in ontologies multiple types of definitions in both formal and in natural languages, but also to ensure that these definitions meet good quality standards so they are useful. While tools such as Protégé can assist in creating well-formed logical definitions, producing good definitions in a natural language is still to a large extent a matter of human ingenuity supported at best by just a small number of general principles. For lack of more precise guidelines, definition authors are often left to their own personal devices. This paper aims to fill this gap by providing the ontology community with a set of principles and conventions to assist in definition writing, editing, and validation, by drawing on existing definition writing principles and guidelines in lexicography, terminology, and logic. 

**Keywords** : Definitions. Ontology. Textual definitions. Definitions in ontologies. Guidelines. Design patterns. Applied ontology. 

Ci.Inf., Brasília, DF, v.46 n.1, p.73-88, jan./abr. 2017 

73 

Guidelines for writing definitions in ontologies 

## **INTRODUCTION** 

Ontologies are being used increasingly to promote reusability of scientific and other sorts of information and to address semantic interoperability issues by integrating heterogeneous data under a common, normalized representation. Definitions play a central role in the use of ontologies both by humans and by computers. Textual definitions allow ontologists and data curators to understand the intended meaning of ontology terms and to use these terms in a consistent fashion across multiple heterogeneous contexts. Definitions formalized in a logical language such as the Web Ontology Language (OWL) allow machines to check the integrity of ontologies and reason over data annotated with ontology terms to make inferences that promote knowledge discovery in areas such as biomedicine. 

Therefore, it is important not only to include in ontologies definitions of both types, but also to ensure that these definitions can be created in a way that will contribute in a reliable fashion to their being useful. 

According to a recent survey we conducted on definition practices in ontologies (SEPPÄLÄ, 2013; SEPPÄLÄ; RUTTENBERG, 2013), ontologists often lack adequate training in definition writing. This may partly explain the disparities in definition coverage observed in the OBO Foundry ontologies. It may also help to explain why so many ontologies lack either or both forms of definition (SCHLEGEL; SEPPÄLÄ; ELKIN, 2016). While tools such as Protégé can assist in creating wellformed logical definitions, producing good natural language definitions is still more a matter of human ingenuity supported at best by just a small number of general definition writing principles. 

Our aim here is to fill this gap by providing the ontology community with a set of principles and conventions to assist in definition writing, editing, and validation. They draw from existing proposals from the disciplines of applied ontology, terminology, lexicography, and logic (ARP; SMITH; SPEAR, 2015; 2009; KELLEY, 1998; 

LANDAU, 2001; NDI-KIMBI, 1994; PAVEL; NOLET, 2001; SMITH, 2013; SVENSÉN, 1993; SWARTZ, 1997; VÉZINA et al., 2009).<sup>1</sup> 

## **SOME PRELIMINARIES ON DEFINITIONS IN GENERAL** 

To make good use of the guidelines which follow, it is important to specify in which way the term _definition_ is used. It is also important to know about the functions of definitions in ontologies. We briefly describe these aspects to provide background for the definition writing guidelines which follow.2 

#### **ONTOLOGICAL DEFINITIONS** 

The purposes of ontological definitions are different from those of definitions in standard dictionaries. In particular, the latter are required to define _all_ lexical items, including those – for example ‘of’, ‘because’, ‘the’ – which do not refer but rather serve structural roles in natural language sentences. Ontological definitions, in contrast, are for ‘terms’, singular noun phrases which are content words that form part of a domain-specific vocabulary used by a group of experts to communicate about entities to which the terms refer. 

#### **HOW IS THE WORD ‘DEFINITION’ USED?** 

The word definition can be used in a number of ways. Here we focus on two: (i) _intension_ and (ii) representational artifact. The former is the content or meaning of the definition and has a counterpart on the side of reality – the set of things, at any given time, to which the definition applies – which is called the _extension_ of a definition. The latter is the form of the definition, the natural language text and potentially the accompanying axioms in some logical formalism that express this meaning. Good definition writing hinges on recognizing that these are the two sides of a single coin. 

1  The present guidelines follow the structure and to some extent the wording of the lexicographic definition writing guidelines prepared for the wordnet community (SEPPÄLÄ, Forthcoming). 2  The preliminaries section is largely based on (SEPPÄLÄ et al., 2016; SEPPÄLÄ; RUTTENBERG; SMITH, 2016; SEPPÄLÄ; SCHREIBER; RUTTENBERG, 2014; SMITH, 2013), which discuss these aspects in more detail. 

Ci.Inf., Brasília, DF, v.46 n.1, p.73-88, jan./abr. 2017 

75 

Selja Seppälä / Alan Ruttenberg / Barry SmitH 

#### **STRUCTURE OF A TEXTUAL DEFINITION** 

When used to refer to the natural language text of a definition, the term ‘definition’ itself can denote different forms: a sentence and a sentence fragment. Broadly, a definition has the canonical form X is a Y that Zs as in example ( **1** ) adapted from the definition of ‘ligament’ (synonym of ‘skeletal ligament’) in the Uberon multi-species anatomy ontology (UBERON). 

- **(1)** A **ligament** is a dense regular connective tissue connecting two or more adjacent skeletal elements. 

Definitions in this form have a three-part structure: 

1. a **definiendum** [ _X_ ], i.e., the defined term; 

2. a **definiens** [ _a Y that Zs_ ], i.e., the part that expresses the definition content and that is called a **definition** in dictionaries; 

3. a **copula** [ _is_ ] that expresses an equivalence between definiendum and definiens. 

In example ( **1** ), ‘ligament’ is the definiendum, which is connected to the definiens “a dense regular connective tissue connecting two or more adjacent skeletal elements” with the copula “is”. Thus, in the wider meaning, ‘definition’ signifies a whole consisting of definiendum, copula, and definiens and takes the linguistic form of a sentence, as in ( **1** ). 

More narrowly, it denotes the **definiens** alone and takes the linguistic form of a sentence fragment, as in ( **2** ): 

- **(2)** Dense regular connective tissue connecting two or more adjacent skeletal elements. (UBERON_0008846) 

The guidelines presented in this paper are concerned with the formulation of the definiens. In dictionaries, definiendum and definiens appear in distinct entry fields and the copula is usually implicit, as in ( **3** ): 

- **(3)** ligament: _Dense regular connective tissue connecting two or more adjacent skeletal elements._ (UBERON_0008846) 

The **definiens** – in italics – is subdivided into at least two parts: 

- The **_genus_ –** _connective tissue –_ which constitutes the head of the definition (the _Y_ part) and tells us what kind of thing the defined term denotes. When the genus is the immediate superordinate term it is called the **_genus proximus_** . 

- One or more **_differentia(e)_** (the _Z_ part(s) or **_distinguishing features_** ) – _dense, regular_ and _connecting two or more adjacent skeletal elements_ – that tell us what characterizes the things referred to by the definiendum and what distinguishes them from the things referred to by the genus term and by all other terms under the same genus. 

Example ( **3** ) thus tells us that “connective tissue” is the genus of the definition of ‘ligament’ and that a ligament is connective tissue of a certain type. The definition has three differentiae, “dense”, “regular” and “connecting two or more adjacent skeletal elements”. These together tell us that ‘ligament’ is more specific than ‘connective tissue’ and that ‘ligament’ differs from other subtypes of connective tissue in virtue of the fact that it is dense and regular and that it has the function of connecting two or . more adjacent skeletal elements 

Each part serves as a condition for determining which things are members of the defined term’s extension. In ontologies, definitions include **_necessary conditions_** that apply to all the members of the extension, but which may also apply to members of other term extensions, and, whenever possible, jointly **_sufficient conditions_ ,** which allow a user to determine whether a given entity is a member of the extension. 

- **(4)** triangle: _A polygon with three edges and three vertices._ (adapted from WIKIPEDIA, 2017) 

This definition tells us that every triangle is necessarily a polygon that has three edges and three vertices, and is sufficient for us to know that anything that is a polygon with three edges and three vertices is a triangle. Together, these 

Ci.Inf., Brasília, DF, v.46 n.1, p.73-88, jan./abr. 2017 

76 

Guidelines for writing definitions in ontologies 

conditions form a **_definition by necessary and jointly sufficient conditions_** , also called a **_classical_** . **_definition_** 

A definition that contains only necessary conditions that are not jointly sufficient to rule out instances that are not members of the extension is called a **_partial definition_** . For example, defining a bird as an animal that lays eggs produces a definition that applies to all instance of birds but also to amphibians. 

#### **FUNCTIONS OF DEFINITIONS** 

Irrespective of the type of resource in which they appear and their context of use, definitions have two primary functions: 

- a _cognitive_ function: to augment or reconfigure (constrain or correct) our knowledge of the world relating to a given term, thus allowing us to better understand a term’s meaning in a specific context of use and create new meaningful semantic connections and interpretations; 

- a _linguistic_ function: to describe or prescribe what we should understand when one or more speakers use the defined term in a specific context of use. 

For example, at the cognitive level, the definition of the term ‘ligament’ in ( **3** ) tells us _what a ligament is_ (some physical object), _what it does_ (it has a connective function), and _what its properties are_ (it has the physical qualities of being dense and regular). At the linguistic level, this definition tells us how the UBERON developers intended us to understand and use the term. 

To fulfill the mentioned functions, the content and form of definitions have to be adapted to each context of use (for example teaching a child to speak, teaching undergraduates in a classroom, or annotating data with an ontology of microbiology) and to the target audience, which in ontologies is for example human curators of databases or developers of natural language processing software. This explains why ontologies have definition types different from those of dictionaries and 

other resources. In ontologies, specifying the intended meaning of a term involves clarifying and disambiguating this meaning so that it can be interpreted by a computer. Definitions in ontologies _stipulate_ and _disambiguate_ the meanings of terms in consistent and non-circular ways. 

For ontologies, the primary context of use requires the inclusion of logical definitions since these are the sorts of definitions needed by a reasoner to perform logical operations, for example, with data annotated with ontology classes. Textual definitions are needed to facilitate ontology development and application by human users. In order to ensure consistency in ontology development and use, the textual and logical definitions of a term must convey the same type of content. This need for parallel semantic content along with the constrained logical properties conferred by the use of necessary conditions give logical definitions additional derived functions that are useful in definition writing and checking: 

- _consistency checking and inference_ : necessary conditions allows us to check whether an instance is consistent with the classes of which it is asserted to be a member, and to infer that the instance has all the properties that are necessary conditions, even if not explicitly stated. 

- _instance classification_ : sufficient conditions allow inferences to be made to the effect that given entities are instances of the class that is being defined; 

- _taxonomic schematization_ : the axioms of a class’s logical definition can be used as a template for the axioms of its subclasses, as well as for the contents of the associated textual definitions; 

- : 

- _• regularizing expression and interpretation of facts_ the controlled vocabulary used in axioms allows us to check the intended meaning of a natural language expression in the textual definition. 

- _avoiding circularity_ : for any given ontology, there should be certain terms accepted as primitive (that are not defined in the ontology); other definitions 

Ci.Inf., Brasília, DF, v.46 n.1, p.73-88, jan./abr. 2017 

77 

Selja Seppälä / Alan Ruttenberg / Barry SmitH 

are then built in a step-by-step manner from these identified primitives (which may be defined in some superordinate ontology). 

It is important to note that the differences between ontology and dictionary definitions result in varied sets of definition correctness criteria. 

## **DEFINITION WRITING GUIDELINES** 

The guidelines we present in this paper are relevant for writing good definitions in ontologies and emphasize textual definitions. The principles are numbered for easy reference and, whenever possible, illustrated with definitions from existing ontologies.<sup>3</sup> The examples include a term (sometimes called a class label), the definition, and the source of the definition – which may be identified through a URI<sup>4</sup> . Our proposed solutions are based on the original definitions, unless otherwise specified. 

## **1. Guideline: CONFORM TO CONVENTIONS** 

Authors should conform to the usual linguistic and lexicographic conventions of the English language (where relevant extended by discipline specific idiolects). 

- ‘Definition’ in what follows means: ‘definiens’. Thus, the definition should not include the term being defined (the definiendum) and it should not include the copula _is_ ; it should be limited to the definiens, a logically connected sentence fragment – see the definition of ‘data set’ in example ( **5** ). 

- A definition should avoid punctuation marks other than commas, but should end with a period if the first letter is capitalized. Uses of other sorts of punctuation – e.g., parentheses, 

> 3  Note that the sources may have been edited since we accessed them on BioPortal (http://bioportal.bioontology.org, accessed July 14, 2017) and OntoBee (http://www.ontobee.org, accessed July 14, 2017). 

colons, slashes (as in ‘and/or’), or semi-colons – are to be avoided, as they detract from the requirement that the definition should be a single logically unitary and unambiguous sentence fragment. 

- Definitions should be written in a natural language supplemented by the technical terms and symbols used in specific disciplines where necessary. 

- Nouns are divided into ‘count’ and ‘mass’ according to whether they can be pluralized (‘cow’ and ‘datum’ are examples of the former; ‘cattle’ and ‘information’ of the latter). Definitions of count nouns should start with an article (‘a’, ‘an’, ‘the’). 

## **1.1. Guideline: HARMONIZE DEFINITIONS** 

Harmonize the definitions in the ontology in order that they all conform to a single set of typographical conventions and editorial guidelines. Example ( **5** ) illustrates a case where the needed consistency is lacking. The definitions of ‘data set’ and ‘measurement datum’ in the Information Artifact Ontology (IAO) should either all be limited to the **_<u>defniens</u>_** (recommended) or all contain the **_defined term_** . **_and the ‘is’ copula_** 

- **(5)** û **data item** : **_A data item is_** _an information content entity that…_ (IAO_0000027) 

   - ü data set: **<u>A data item that is</u>** <u>an aggregate of other data items of the same type that… (IAO_0000100)</u> 

   - û **measurement datum** : **_A measurement datum is_** _an information content entity that…_ (IAO_0000109) 

Where it is agreed by the ontology editors that a specified limited vocabulary will be used in definitions, the wording of the definitions should also be checked to ensure conformance. 

> 4  The ontologies referenced in the examples are listed at the end of the guidelines. All the CURIEs are prefixed with http://purl. obolibrary.org/obo/ unless otherwise specified in the ontology reference list. 

Ci.Inf., Brasília, DF, v.46 n.1, p.73-88, jan./abr. 2017 

78 

Guidelines for writing definitions in ontologies 

## **2. Guideline: PRINCIPLES OF GOOD PRACTICE** 

The following are principles for working with definitions that should be followed to promote good practice. 

- Very high-level ontologies will have many terms — such as ‘entity’ — which are so general that they are not capable of being defined without circularity; these should be marked as ‘primitive’; they should be accompanied by elucidations and examples of use. 

- Definitions should be unique (i.e., no two terms in a single ontology should share what is, logically speaking, the same definition).<sup>5</sup> 

- When referring to other classes, use the controlled vocabulary specified in the ontology (i.e., the terms in the ontology labels) to produce consistently written definitions across the ontology. 

- Include a single definition per class. This means that there should be a single ‘definition’ annotation property (IAO_0000100), which should contain a single definition (see also principle 6.2). 

- Cite your sources and do it in a separate annotation property, preferably using the IAO ‘definition source’ annotation property (IAO_0000119). 

- Credit authorship, preferably using the IAO ‘term editor’ annotation property (IAO_0000117). 

**3. Guideline: USE THE GENUSDIFFERENTIA FORM** 

A definition should have the genus-differentia form, where the genus anchors the defined entity to a known entity at a higher level of generality, and the differentia (or differentiae) picks out those cases within this higher level 

> 5 _OBO Foundry Principles: Textual Definitions_ at http://obofoundry.org/ principles/fp-006-textual-definitions.html [accessed: July 14, 2017]. 

that fall under the term defined. In example ( **6** ), only the first definition of mammal is correctly structured. It has a **_genus_** and three _<u>diferentiae</u>_ <u>;</u> the second definition only has a genus followed by example subtypes; the last definition lacks a genus (including the definiendum instead) and has one differentia. 

- **(6)** ü mammal: **_a vertebrate_** _<u>that has hair, gives live birth,</u> and nurses its young_ 

- û mammal: **_a vertebrate_** _like, a cat, dog, or whale_ 

   - û mammal: _Mammals_ _<u>nurse their young.</u>_ 

## **3.1. Guideline: INCLUDE EXACTLY ONE GENUS** 

A definition should always have one and only one genus ( **7** ). The genus is a superordinate term that tells us with what kind of thing we are dealing. Definitions of things like colors are expressed in the nominal form and start with a genus such as “a quality”. Similarly, definitions of processes and other entities that unfold in time, which are often expressed by verbs are, in ontologies, defined with nominal phrases. 

In example ( **7** ), the definition of ‘recombinant vector’ in the Ontology for Biomedical Investigations (OBI) does not have a genus. This can be fixed by adding its _genus proximus_ , which in OBI is ‘processed material’. 

- **(7)** û recombinant vector: _A recombinant vector_ **_is created by_** _a recombinant vector cloning process, …_ (OBI_0000731) 

   - ü recombinant vector: **_A processed material_** created by a recombinant vector cloning process, … 

- **3.1.1. Guideline: USE THE** **_GENUS PROXIMUS_** 

Use the _genus proximus_ , that is, the closest parent term. This ensures that the genus is specific enough and that all the terms at the same level have the same genus. 

Ci.Inf., Brasília, DF, v.46 n.1, p.73-88, jan./abr. 2017 

79 

Selja Seppälä / Alan Ruttenberg / Barry SmitH 

As an ontology is developed and new classes interposed between existing levels, the _genus proximus_ may also change and the corresponding definitions need to be updated.  Example ( **8** ) shows two definitions of sibling classes: the definition of ‘data set’ includes the correct _genus proximus_ (‘data item’), whereas the definition of ‘measurement datum’ does not, as it includes the parent of its _genus proximus_ (‘information content’). 

- **(8)** û **data item** : _A data item is an_ **_information content entity_** _that…_ (IAO_0000027) 

data set: _A_ **_data item_** _that…_ (IAO_0000100) measurement datum: _A measurement datum is an_ **_information content entity_** _that…_ (IAO_0000109) 

- ü **data item** : _An_ **_information content entity_** _that…_ 

data set: _A_ **_data item_** _that…_ 

measurement datum: _A_ **_data item_** _that…_ 

## **3.1.2. Guideline: AVOID PLURALS** 

The genus of a definition should have the same syntactic properties as the definiendum. According to the naming conventions contained in the OBO Foundry Principles,<sup>6</sup> which are also in line with good terminology practice accepted elsewhere, terms in ontologies should be written “as if writing in plain English”. This includes writing them in the singular form. Therefore, the genus of a definition should also be in the singular form. In example ( **9** ), the definition of ‘myeloablative agonist’ in the National Cancer Institute Thesaurus (NCIt) has a plural genus, which can be replaced by its singular form. Note that the rest of the definition needs to be adapted to accommodate this change.<sup>7</sup> 

> 6 _OBO Foundry Principles: Naming Conventions_ at http:// obofoundry.org/principles/fp-012-naming-conventions.html [accessed: June 21, 2017]. 

7  In the corrected version of this example, we also edited the rest of the definition to comply with the single fragment principle. 

- **(9)** û Myeloablative Agonist: **_Agents_** _that destroy bone marrow activity. They are used to prepare patients for bone marrow or stem cell transplantation._ (NCIt:C1711) 

   - ü myeloablative agonist: **_An agent_** _that destroys bone marrow activity and that is used to prepare patients for bone marrow or stem cell transplantation._ 

## **3.13. Guideline: AVOID CONJUNCTIONS AND DISJUNCTIONS** 

The genus of a definition should be a single word: not a conjunction ( **10** ) and also not a disjunction ( **11** ). A conjunction or disjunction in a genus can be avoided by using a more general genus ( **10** ) and, if applicable, by adding a differentia specifying the things denoted by the conjunction or disjunction, as in ( **11** ). In example ( **10** ), we avoid the conjunction by using a more general term and adding the elements of the conjunction as differentia – note that the new genus might have to be added to the ontology if it falls within its scope. In example ( **11** ), we avoid the disjunction by using a parent term. 

- **(10)** û Cell Culture System: **_Systems and reagents_** _for the propagation of cells in tissue culture._ (NCIt:C19147) 

   - ü cell culture system: **_A system_** _comprising reagents and other systems which together enable propagation of cells in tissue culture._ 

- **(11)** û analyte: _The_ **_sample or material_** _being subjected to analysis._ (NCIt:C128639) 

   - ü analyte: _A_ **_spe/cimen_** _being subjected to analysis._ 

## **3.1.4. Guideline: AVOID CATEGORIZERS** 

The role of the genus of a definition is to categorize the denoted thing under a more general type. Therefore, it is not necessary to add an extra categorizing expression, such as “type of” and “sort of”. These can usually be omitted, as in ( **12** ). 

Ci.Inf., Brasília, DF, v.46 n.1, p.73-88, jan./abr. 2017 

80 

Guidelines for writing definitions in ontologies 

- **(12)** û immunogen: **_A type of antigen_** _capable on its own of inducing an immune response._ (CHEBI_60816) 

   - ü immunogen: **_An antigen_** _capable, on its own, of inducing an immune response._ 

## **4. Guideline: AVOID USE/MENTION CONFUSION** 

A definition should tell us about the thing that is denoted by the definiendum, not about the term itself or the class that represents the defined thing. Making this confusion is called the **_use/ mention confusion_** . It is illustrated in examples ( **13** ) and ( **14** ). 

- **(13)** û miosis AE: _Miosis AE is an eye AE that_ **_is a term with various definitions_** _, which generally include constriction of the pupil._ (OAE_0001998) 

   - ü miosis AE: _An eye AE that generally includes constriction of the pupil._ 

- **(14)** û mammal _:_ **_Representation_** _of an animal that feeds its young with milk._ (ARP; SMITH; SPEAR, 2015) 

   - û mammal _:_ **_A term that refers to_** _an animal that feeds its young with milk._ 

   - ü mammal: **_An animal_** _that feeds its young with milk._ 

The first two examples in ( **14** ) confound the class and the term with the thing that they represent, respectively. 

**5. Guideline: INCLUDE NECESSARY AND, WHENEVER POSSIBLE, JOINTLY SUFFICIENT CONDITIONS** 

Definitions should avoid non-defining information. They must consist exclusively of necessary conditions which should, whenever possible, be jointly sufficient. 

#### **5.1. Guideline: AVOID ENCYCLOPEDIC INFORMATION** 

Definitions should avoid including information that goes beyond the minimum useful information for specifying the intended meaning of a term ( **15** ). They should also avoid 

including information about the use of a term ( **16** ). In ontologies, any type of information that goes beyond what is or should be expressed by the axioms may be considered encyclopedic. This kind of information might be useful for understanding a term’s intended meaning or its use or is deemed otherwise useful for the target audience but it is not defining information and so should not be included in a definition. Often, an indication that a piece of information is encyclopedic is that it cannot be expressed as a necessary condition. Such information should be included in a separate annotation property, such as ‘editor note’ (IAO_0000116) or ‘example of usage’ (IAO_0000112). 

- **(15)** û spiracle: _An orifice of the tracheal system by which gases enter and leave the body._ **_Ants have 9 or 10 spiracles on each side of the body. The prothoracic spiracles have been lost, so the first opening occurs on the mesothroax._** (SIBO_0000502) 

   - ü spiracle: _An orifice of the tracheal system by which gases enter and leave the body._ **Editor note:** Ants have 9 or 10 spiracles on each side of the body. The prothoracic spiracles have been lost, so the first opening occurs on the mesothroax. 

- **(16)** û complex: _Set of interacting molecules that can be copurified._ **_This term and its children should be used only at PARTICIPANT level._** (MI_0314) 

   - ü complex: _Set of interacting molecules that can be copurified._ **Editor note:** This term and its children should be used only at PARTICIPANT level. 

## **5.2. Guideline: AVOID NEGATIVE TERMS** 

_is not_ is A definition that tells us what something uninformative; it should tell us what something _is_ . Therefore, a definition should not include negative features, which should be avoided by stating positive characteristics of the defined entity ( **17** ). However, there are at least two 

Ci.Inf., Brasília, DF, v.46 n.1, p.73-88, jan./abr. 2017 

81 

Selja Seppälä / Alan Ruttenberg / Barry SmitH 

exceptions to this principle: (i) when the defined entity is inherently negative ( **18** ) and (ii) when the negative feature is a distinguishing feature between two sibling classes ( **19** ). 

- **(17)** û mineral: _composed of matter_ **_other than plant or animal_** (WordNet 3.1) 

   - ü mineral: _Composed of solid inorganic matter._ 

- **(18)** ü non-parametric test: _A statistical hypothesis test_ **_that is not based on any parameterized family of probability distributions_** _._ (OBCS_0000236) 

   - ü bachelor: _A man who_ **_is not married_** _._ 

- **(19)** ü paracentric inversion: _A chromosomal inversion_ **_that does not include the centromere_** _._ (SO_1000047) pericentric inversion: _A chromosomal inversion_ **_that includes the centromere_** _._ (SO_1000046) 

## **5.3. Guideline: AVOID DEFINITIONS BY EXTENSION** 

Definitions by extension ( **20** ) list instances, i.e., members of the definition’s extension, and do not tell us what the thing being defined is, unless we are already familiar with the listed instances. To be maximally informative, use definitions by intension that specify characteristics of the defined thing, as in the corrected version of ( **20** ). 

- **(20)** û planet: _Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune._ 

   - ü planet: _A celestial body in orbit around the Sun that has a nearly round shape and has cleared the neighborhood around its orbit_<sup>8</sup> _._ 

> 8 Adapted from the 2006 definition of planet by the International Astronomical Union (IAU). 

## **6. Guideline: ADJUST THE SCOPE** 

Definitions should have the appropriate scope. 

## **6.1. Guideline: A DEFINITION SHOULD BE NEITHER TOO BROAD NOR TOO NARROW** 

A definition that is too broad includes things that are not in the extension of the term being **21** defined ( ). A definition that is too narrow fails to include things that are in the extension of the term being defined ( **22** ). 

- **(21)** û bird: _an animal that lays eggs_ (KELLEY, 1998) 

   - ü bird: _warm-blooded egg-laying vertebrate with feathers and with wings that evolved from forelimbs_ (adapted from WordNet 3.1) 

In example ( **21** ), the first definition of bird would be too broad since it includes all oviparous animals, i.e., fish, birds, reptiles and insects. By contrast, the above definition has an adequate scope. 

- **(22)** û antidote: _a substance that counteracts snakebite_ (KELLEY, 1998) 

   - ü antidote: _a remedy that stops or controls the effects of a poison_ (WordNet 3.1) 

In example ( **22** ), the first definition of antidote would be too narrow since it excludes other types of poison form its extension. By contrast, the WordNet 3.1 definition of antidote has an adequate scope. 

## **6.2. Guideline: DEFINE ONLY ONE THING WITH A SINGLE TEXTUAL DEFINITION** 

A definition should define only one thing. Therefore, a class should have a single textual definition. Two cases that should be avoided are often found: (i) nested definitions, where definitions contain definitions of other terms embedded within them ( **23** ), and (ii) multiple definitions, where a single definition annotation property contains definitions in addition to the primary definitional sentence fragment ( **24** ). Such cases might indicate that a new class should be added to the ontology. If the additional definition is 

Ci.Inf., Brasília, DF, v.46 n.1, p.73-88, jan./abr. 2017 

82 

Guidelines for writing definitions in ontologies 

of an entity that falls within the scope of the ontology, we recommend either (i) removing the additional definition from the annotation property and adding it as the definition of a new term, then using that in the first definition, as in ( **24** ), (ii) if the class already exists in the ontology, use the class in the primary definition and delete the additional definition ( **23** ). If the additional definition is of an entity that is out of the scope of the ontology, we recommend either (i) if the term exists in another ontology, using MIREOT (COURTOT et al., 2011) to import the term and then using it, (ii) adding it into a separate editor note, (iii) deleting the additional definition, or (iv) replacing the term deemed to be unknown to the reader with its definition, as in the second solution in ( **23** ). 

Whenever the term is already in the ontology, a crossreference is preferable since it preserves the link to the full definition of the potentially problematic entity introduced in the definition, as well as to the term that denotes it, both of which are lost when the term is replaced by its definition. Replacing the term by its definition may cause issues if the corresponding class is deprecated and the definition must be updated. It is more difficult to find an embedded definition than it is to identify a term in a definition. 

- **(23)** The WordNet 3.1 definition of _cytolytic_ , which contains a nested definition of _cytolysis_ , can be edited as follows: 

   - û<sup>cytolytic:</sup><sup>_of or relating to_</sup><sup>**_cytolysis_**</sup><sup>_,_</sup><sup>**_the_**</sup> **_dissolution or destruction of a cell_** (WordNet 3.1) 

   - ü cytolytic: _of or relating to_ **_<u>cytolysis</u>_** 

   - ü cytolytic: _of or relating to_ **_the dissolution or destruction of a cell_** 

- **(24)** û cell measurement: _Any quantification of a morphological or physiological parameter of one or more cells._ **_A cell is a membraneenclosed protoplasmic mass constituting the smallest structural unit of an organism that is capable of independent functioning._** (CMO_0000227) 

   - ü cell measurement: _Any quantification of a morphological or physiological parameter of one or more_ **_<u>cells</u>_** _._ 

#### **cell:** **_A membrane-enclosed protoplasmic mass constituting the smallest structural unit of an organism that is capable of independent functioning._** 

## **7. Guideline: AVOID CIRCULARITY** 

For a definition to be informative, it should avoid circularity. Circularity can manifest itself in two ways: within the same definition or within the system of definitions. 

Circularity within the same definition occurs when a class is defined in terms of itself using one of the labels attached to the class ( **25** ) or a synonym thereof ( **26** ), or some grammatically derived form, as in ( **27** ) when _fearful_ is not separately defined independently of _fear_ . 

- **(25)** û training objective: _A_ **_training objective_** _which is fulfilled by the provision of some training_ (OBI_0000962) 

   - ü c training objective: _An_ **_objective_** _which is fulfilled by the provision of some training._ 

- **(26)** û large: _The attribute of something that is_ **_big_** _._ (KELLEY, 1998) 

   - ü large: _The attribute something_ **_has when it has a measurable quality that is above average_** _._ (adapted from the definition of _large_ in WordNet 3.1) 

- **(27)** û fear: _The state of being_ **_fearful_** _._ (LANDAU, 2001) 

   - ü fear: **_an emotion experienced in anticipation of some specific pain or danger_** (WordNet 3.1) 

Circularity within the system of definitions occurs when terms are defined in terms of each other, forming a circular pair ( **28** ) or a circular chain of definitions. 

- **(28)** û **training objective** : _A training objective which is fulfilled by the provision of some_ **_training_** (OBI_0000962) 

   - **training process** : _A process that achieves a_ **_training objective_** (OBI_0000962) 

Ci.Inf., Brasília, DF, v.46 n.1, p.73-88, jan./abr. 2017 

83 

Selja Seppälä / Alan Ruttenberg / Barry SmitH 

In example ( **28** ), the pair of circular definitions tell us that a training objective is fulfilled by some training (process) and that a training process achieves a training objective. It does not tell us what either of these things really are. 

- ü increased activity of parathyroid: _Increased function of the paired endocrine gland that produces parathyroid hormone (PTH) that regulates calcium and phosphorous metabolism._ 

## **8. Guideline: INCLUDE JOINTLY SATISFIABLE FEATURES** 

The stated conditions must be jointly satisfiable (ARP; SMITH; SPEAR, 2015), that is 

- the entity defined must have instances ( **29** ), 

- there should be no logical contradictions involved ( **29** ). (ARP; SMITH; SPEAR, 2015) 

   - û round square: **_A geometric figure that is simultaneously round and square shaped._** 

- **(29)** 

## **9. Guideline: USE APPROPRIATE DEGREE OF GENERALITY** 

A definition should be general. 

## **9.1. Guideline: AVOID GENERALIZING EXPRESSIONS** 

Avoid the use of expressions such as “usually” and “generally” since either 

- a definition is already a statement of general knowledge about a typical case (e.g., in biology) ( **30** ); or 

- the feature containing the expression is not a defining feature, but rather an encyclopedic piece of information that can be moved to a separate ‘editor note’ annotation property ( **31** ). 

- **(30)** û increased activity of parathyroid: _increased function of this paired endocrine gland that_ **_normally_** _produces parathyroid hormone (PTH) that regulates calcium and phosphorous metabolism_ (MP_0003432) 

- **(31)** û Tumor Lysis Syndrome: _A syndrome resulting from cytotoxic therapy,_ **_occurring generally in aggressive, rapidly proliferating lymphoproliferative disorders_** _. It is characterized by combinations of hyperuricemia, lactic acidosis, hyperkalemia, hyperphosphatemia and hypocalcemia._ (MESH:D015275) 

   - ü tumor lysis syndrome: _A syndrome resulting from cytotoxic therapy, characterized by combinations of hyperuricemia, lactic acidosis, hyperkalemia, hyperphosphatemia and hypocalcemia._ **Note: Tumor lysis syndrome occurs generally in aggressive, rapidly proliferating lymphoproliferative disorders.** 

## **9.2. Guideline: AVOID EXAMPLES AND LISTS** 

Avoid using examples and expressions that specify or enumerate examples (or counterexamples) of things within the definition, such as “etc.”, “for example”, and “such as”, whether it applies (i) to members of the definition’s extension ( **32** ) or (ii) to various types of things falling under the extension of a distinguishing feature, as in ( **33** ). In the first case, the example(s) should be included in a separate annotation property, such as ‘example’ (IAO_0000112). In the second case, when possible, replace the examples in the definition with a more general term, the extension of which includes all the examples, as in ( **33** ). 

- **(32)** û cellular_organism: _An organism of microscopic or submicroscopic size,_ **_<u>especially a bacterium or</u> protozoan_** (NCRO_0000483) 

Ci.Inf., Brasília, DF, v.46 n.1, p.73-88, jan./abr. 2017 

84 

Guidelines for writing definitions in ontologies 

- ü cellular organism: _An organism of microscopic or submicroscopic size._ **Examples: a bacterium; a protozoan** 

In example ( **32** ), bacterium and protozoan are examples of cellular organisms introduced by the expression “especially”. 

- **(33)** û patient questionnaire: _A questionnaire that comprises a set of_ **_questions about a patient, such as height, weight, race, biological sex, clinical history,_** **_<u>etc.</u>_** _<u>, which will be filled by</u> the human subject._ (OBIB_0000020) 

   - ü patient questionnaire: _A questionnaire that comprises a set of_ **_demographic and medical questions_** _, which will be filled by the human subject._ 

In example ( **33** ), “etc.” marks the presence of examples listed to illustrate the types of questions that are part of a questionnaire (i.e., the extension of a differentia). These examples can be replaced by more general terms. 

## **9.3. Guideline: AVOID INDEXICAL AND DEICTIC TERMS** 

Avoid indexical and deictic terms, such as ‘today’, ‘here’, and ‘this’ when they refer to (the context of) the author of the definition or the resource itself. Such expressions often indicate the presence of a non-defining feature or a case of use/mention confusion. Most of the times, the definition can be edited and rephrased in a more general way ( **34** ). 

- **(34)** û hypersecretion of corticotropinreleasing hormone: _excessive release of_ **_this_** _factor, which normally stimulates the pituitary to release adrenocorticotropic hormone, from the hypothalamus_ (MP_0001753) 

   - ü hypersecretion of corticotropinreleasing hormone: _Excessive release of corticotropin-releasing hormone from the hypothalamus._ Editor note: corticotropin-releasing hormone normally stimulates the pituitary to release adrenocorticotropic hormone 

## **9.4. Guideline: AVOID SUBJECTIVE AND EVALUATIVE STATEMENTS** 

Definitions should avoid any kind of subjective and evaluative language, as in ( **35** ) where the words ‘delicious’ and ‘beautiful’ are removed from the definition without any change in the informative content. 

- **(35)** û cranberry bean: _Also called shell bean or shellout, and known as borlotti bean in Italy, the cranberry bean has a large, knobby beige pod splotched with red. The beans inside are creamcolored with red streaks and have a_ **_delicious_** _nutlike flavor. Cranberry beans must be shelled before cooking. Heat diminishes their_ **_beautiful_** _red color. They’re available fresh in the summer and dried throughout the year._ (FOODON_03411186) 

   - ü cranberry bean: _A bean that has a large, knobby beige pod splotched with red, that is cream-colored with red streaks, and has a nutlike flavor._ 

Synonyms: shell bean; shellout; borlotti bean Editor note: Cranberry beans must be shelled before cooking. Heat diminishes their beautiful red color. They’re available fresh in the summer and dried throughout the year. 

## **10. Guideline: DEFINE ABBREVIATIONS AND ACRONYMS** 

Abbreviations and acronyms should be defined not explicated ( **36** ). In most cases, the full form of the term should be added as the preferred term using the ‘editor preferred term’ (IAO_0000111) annotation property, and the abbreviation or acronym added as a synonym label using ‘alternative term’ (IAO_0000118). Note that in ( **36** ) ‘laser’ can be kept as the preferred term since the acronym has become lexicalized. 

Ci.Inf., Brasília, DF, v.46 n.1, p.73-88, jan./abr. 2017 

85 

Selja Seppälä / Alan Ruttenberg / Barry SmitH 

- **(36)** û laser: _A_ **_laser (acronym for light amplification by the stimulated emission of radiation)_** _is a light source that…_ (OBI_040064) 

   - ü laser: _A light source that…_ **Alternative term: light amplification by the stimulated emission of radiation** 

#### **Editor note: “laser” is an acronym** 

## **11. Guideline: Match Textual and Logical Definitions** 

Since textual and logical definitions are meant to specify the intended meaning of an ontology’s terms, they should _in principle_ include the same type of information, although in some cases the logical definition might have additional axioms that help reasoning but which otherwise might be considered inessential. To ensure consistency in ontology development and use, and to promote cohesion across definitions, it is recommended that the parts of a given textual definition match the parts of the corresponding logical definition as in ( **37** ). However, the parts need not appear in the same order. 

## **11.1. Guideline: Proofreading Definitions** 

Always check the spelling and grammar using appropriate tools. In example ( **38** ), the definition of ‘anesthesiology residency program’, ‘specialty’ is misspelled and ‘administration’ is spelled incorrectly in two different ways (see words in bold). This could be easily rectified by running a spellchecker. 

   - **(38)** ü anesthesiology residency program: _A medical residency in the medical_ **_speciality_** _that focuses on the_ **_administeration_** _of medication for the temporary general or local suppression of sensory or motor nerve function during some health care encounter or on making decisions regarding the_ **_adminstration_** _of such medication._ (OOST_00000232) 

- **(37)** ü bacteremia: _<u>An infection that has as part bacteria located in the blood.</u>_ (IDO_0000506) 

bacteremia **EquivalentTo** infection **and (has_part some (infectious agent and Bacteria and (located_in some blood)))** 

Ci.Inf., Brasília, DF, v.46 n.1, p.73-88, jan./abr. 2017 

86 

Guidelines for writing definitions in ontologies 

## **FINAL REMARKS** 

The objective of these guidelines was to provide the applied ontology community with the relevant principles and conventions for good definition practices in ontologies. These guidelines were also meant to give basic foundational background knowledge on definitions to help readers understand the rationale behind these principles. Finally, these definition writing guidelines have the added benefit of serving as a verification tool for existing ontology definitions. 

## **ACKNOWLEDGEMENTS** 

This work was supported in part by the Swiss National Science Foundation (SNSF), by the NIH/ NCATS Clinical and Translational Science Awards to the University of Florida UL1 TR000064, and by the University at Buffalo UL1 TR001412. The content is solely the responsibility of the authors and does not necessarily represent the official views of the SNSF, the National Institutes of Health, or the NCTE. Many thanks also to Amanda Hicks, Mark Jensen, Daniel R. Schlegel, and Patrick Ray for their useful discussions and comments and their contributions with examples. 

## **REFERENCES** 

ARP, R.; SMITH, B.; SPEAR, A. D. _Building ontologies with basic formal ontology_ . Cambridge, MA: MIT Press, 2015. 

COURTOT, M. et al. Mireot: the minimum information to reference an external ontology term. _Applied Ontology_ , v. 6, n. 1, p. 23-33, 2011. 

INTERNATIONAL ORGANIZATION FOR STANDARDIZATION - ISO. _Terminology work:_ principles and methods (iso 704:2009). Geneva:  ISO, 2009. 

KELLEY, D. _The art of reasoning._ Third edition. New York, London: W.W. Norton & Company, 1998. 

LANDAU, S. I. _Dictionaries:_ the art and craft of lexicography. 2nd editon. Cambridge: Cambridge University Press, 2001. 

NDI-KIMBI, A. Guidelines for terminological definitions: the adherence to and deviation from existing rules in bs/iso 2382: data processing and information technology vocabulary. _Terminology_ , v. 1, n. 2, 1994. p. 327-350. 

PAVEL, S.; NOLET, D. _Handbook of terminology_ . Canada: Public Works and Government Services - Translations Bureau, 2001. 

SCHLEGEL, D. R.; SEPPÄLÄ, S.; ELKIN, P. L. Definition coverage in the obo foundry ontologies: the big picture. In: _Proceedings of the International Workshop on Definitions in Ontologies_ (ICBO BioCreative 2016), August 1-4, Corvallis (ORG), USA, 2016. 

SEPPÄLÄ, S. Survey on defining practices in ontologies: Report summary. In: _Proceedings of the International Workshop on Definitions in Ontologies_ (DO 2013), 2013, Montreal, Canada. 2013. 

__________. Definition writing guidelines for cili. _Linguistic Issues in Language Technology (LiLT)_ , Special Issue on on Linking, Integrating and Extending Wordnets. Forthcoming. 

__________; RUTTENBERG, A. _Survey on defining practices in ontologies:_ report, 2013. Available at: <http:// definitionsinontologies.weebly.com/survey-report.html>. Accessed on: 30 nov. 2017. 

__________.; __________.; SCHREIBER, Y.. Definitions in ontologies. _Cahiers de lexicologie_ , n. 109, p. 173-206, 2016. 

__________; SMITH, B. The functions of definitions in ontologies. In: _Formal ontology in information systems_ : Proceedings of the 9th international conference (FOIS 2016), v. 283. FERRARIO R.; KUHN, W. (ED). Annecy, France: IOS Press, 2016. p. 37-50. 

__________; SCHREIBER, Y.; RUTTENBERG, A. Textual and logical definitions in ontologies. In: _Proceedings of The First International Workshop on Drug Interaction Knowledge Management_ (DIKR 2014), 1., _The Second International Workshop on Definitions in Ontologies_ (IWOOD 2014), and _The Starting an OBI-based Biobank Ontology Workshop_ (OBIB 2014), October 6-7, Houston, TX, USA. 2014. 

SMITH, B. Introduction to the logic of definitions. In: _Proceedings of the International Workshop on Definitions in Ontologies_ (DO 2013),) in _Proceedings of the 4th International Conference on Biomedical Ontology Workshops_ (ICBO 2013), v. 1061, July 7, Montreal, Canada. 2013. 

SVENSÉN, B. _Practical lexicography:_ principles and methods of dictionarymaking. Oxford England; New York: Oxford University Press, 1993. 

SWARTZ, N. _Definitions, dictionaries and meanings._ 1997. Available at: <http://www.sfu.ca/~swartz/definitions.htm>. Accessed on: 14 jul. 2017. 

VÉZINA, R. et al. _La rédaction de définitions terminologiques_ . Montréal: Office québecois de la langue française, 2009. 

WIKIPEDIA. _Triangle:_ wikipedia, the free encyclopedia, 2017. Available at: <https://en.wikipedia.org/w/index. php?title=Triangle&oldid=785338335>. Accessed on: 31 jul. 2017. 

Ci.Inf., Brasília, DF, v.46 n.1, p.73-88, jan./abr. 2017 

87 

Selja Seppälä / Alan Ruttenberg / Barry SmitH 

## **ANNEX** 

#### **ONTOLOGIES REFERENCED IN THE EXAMPLES** 

Unless otherwise specified below, all the cited identifiers of terms from these ontologies are CURIEs,9 with the prefix http://purl.obolibrary.org/obo/. 

- CHEBI: Chemical Entities of Biological Interest 

- CMO: Clinical Measurement Ontology 

- DDANAT: Dictyostelium discoideum anatomy 

- EFO: Experimental Factor Ontology (prefix http://www.ebi.ac.uk/efo/) 

- FOODON: FoodOntology (FoodOn) 

- IAO: Information Artifact Ontology 

- MESH: Medical Subject Headings (MeSH) (prefix MESH=http://purl.bioontology.org/ontology/MESH) 

- MI: Molecular Interactions 

- MP: Mammalian Phenotype Ontology 

- NCIt: National Cancer Institute Thesaurus (prefix NCIt=http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#) 

- NCRO: Non-Coding RNA Ontology 

- OAE: Ontology of Adverse Events 

- OBCS: Ontology of Biological and Clinical Statistics 

- OBI: Ontology for Biomedical Investigations 

- OBIB: Ontology for Biobanking 

- OOST: Ontology of Organizational Structures of Trauma centers and Trauma systems 

- SIBO: Social Insect Behavior Ontology 

- SO: Sequence Types and Features Ontology 

- UBERON: Uberon multi-species anatomy ontology 

> 9  CURIE Syntax 1.0: A syntax for expressing Compact URIs, W3C Working Group Note 16 December 2010 (https://www.w3.org/TR/ curie/, accessed July 14, 2017) 

Ci.Inf., Brasília, DF, v.46 n.1, p.73-88, jan./abr. 2017 

88 

