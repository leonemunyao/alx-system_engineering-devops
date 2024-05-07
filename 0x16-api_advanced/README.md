0x16. API advanced

Listing

Many endpoints on reddit use the same protocal for controlling pagination and filtering. These endpoints are called listing and share five common parameters: after / before, limit, count , and show. Listings allow you to view slices of underlying data. Listing JSON responses contain after and before fields which are equivalent to to the next and prev buttons on the site and in combining with cout can be used to page through the listing.

The common parameters are as folows;

: after / before - only one should be specified, these indicates the fullname of an item in the listing to use as the anchor point of 
    the slice.
: limit - maximum number of items to return in the slice of the listings.
: count - the number of items already seen in the listing. on the html site the builder uses this to determine when to give values for before and after in the response.

Modhashes

A modhash is a token the reddit API requires to help prevent CSRF(Cross-Site Request Forgery). Modhashes can be obtained via the /api/me.json call or in response data of listing endpoints.

Fullnames

A fullname is a combination of a thing's type and its unique ID which forms a compact encoding of a globally unique ID on reddit. Type prefixes can be t1_ for comment, t2_ for account, t3_ for link, t4_ for message, t5_ for subreddit, t6_ for award. 


Query String 

A query string is a part of a uniform resource locator.(URL) that assigns values to specifed parameters. It includes fields added to a base URL by a web browser or other client application. A typical URL containing a query string is as follows, htpps://example.com/over/there?name=ferret . The querry string n this case is name=ferret . The question mark is used as separator and its not part of the query string.

Multiquery parameters are separated by ampersand "&" . https://example.com/path/to/page?name=ferret&color=purple 
