# ddi-maDMP-mapping
prototype ddi-maDMP mapping

## Objective

Create a ddi codebook 2.5 mapping to and from maDMP prototype using sssom.

## Usage of the SSSOM standrd to describe mappings

We try as mutch as possible to stick to the standard defintion, but there are
some small changes to this rule (see below). Basically, in a tsv mappinga file
we use the format "[namespace:]xpath" to identify subject_ids and object_ids. 

## Additions to the SSSOM standard

As SSSOM was built to map ontologies it is not directly usable to map file types,
but there is a basic solution to this, in addition to the sssom required fields 
the user has to add 4 supplementary fields subjects and object types and cardinalities, so:

**In a mapping under the field "other" we require the addition of 4 keys:**
	
- subject_cardinality
- subject_type
- object_cardinality
- object_type
    
**valid values:**

cardinalities = ["0..1", "1", "0..n", "1..n", "n"]

first number representis minimum, the second the maximum. If the minimum and the
maximum are the same then only "1" or "n" are used instead of "1..1" and "n..n".

types = ["literal", "voc", "object", "list"]



## DDI mappings to convet to the SSSOM format:

https://github.com/MetadataTransform/ddi-xslt

https://zenodo.org/record/6505238#.ZB9Z58ZwFt0



## Resources

https://mapping-commons.github.io/sssom/

https://www.w3.org/TR/swbp-skos-core-spec/

https://ddialliance.org/Specification/DDI-Codebook/2.5/

https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard
