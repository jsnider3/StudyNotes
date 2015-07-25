### MongoDB Notes

* A database of "documents" in order to reduce the need for joins.
* Documents are maps of fields to values, values can be arrays or
  arrays of documents. This is different from Python maps somehow?
* Designed to be high-performance. Isn't everything? 
* Designed to be cloudy and easy to scale using "shards".
* Open-source like all good systems.
* It's a NoSQL database, so objects can be whatever. 
* Documents can either have subdocuments (like embedded structs)
  or have references to other documents.
  * When designing its important to know when to choose which of these.
* Write operations are guaranteed to be atomic at the document level.(!!)
* Embedded documents are better when one is a "container" of the other.
  This is similar to denormalization in other databases. One-to-one.
* Embedded documents are bad when it leads to data fragmentation and
  sprawl.
* References are similar to normalization in other databases. Works
  best with shared data in a many-to-many relation. More flexible, but
  forces applications to use more queries to look things up.


