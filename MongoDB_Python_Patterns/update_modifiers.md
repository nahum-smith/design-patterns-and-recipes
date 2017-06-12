# MongoDB Update Modifiers
Modifier | Meaning | Example
--- | --- | --- 
$inc | Atomic Increment | “$inc”:{"score”:1}
$set | Set Property Value | “$set”:{"username”:"niall"}
$unset | Unset (delete) Property | “$unset”:{"username”:1}
$push | Atomic Array Append (atom) | “$push”:{"emails”:"foo@example.com"}
$pushAll | Atomic Array Append (list) | “$pushall”:{"emails”:["foo@example.com”,"foo2@example.com"]}
$addToSet | Atomic Append-If-Not-Present | “$addToSet”:{"emails”:"foo@example.com"}
$pop | Atomic Array Tail Remove | “$pop”:{"emails”:1}
$pull | Atomic Conditional Array Item Removal | “$pull”:{"emails”:"foo@example.com"}
$pullAll | Atomic Array Multi Item Removal | “$pullAll”:{"emails”:["foo@example.com”, “foo2@example.com"]}
$rename |Atomic Property Rename | “$rename”:{"emails”:"old_emails"}
