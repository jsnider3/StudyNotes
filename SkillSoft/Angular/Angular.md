# Angular.js Services

If you don't like ng's everywhere, this is not the
tutorial for you.

Angular has a bunch of services built-in. These are like
libraries, but as objects. You can make your own services
if you want and I expect that to be a common thing for
professional web developers.

Angular-js is a huge fan of dependency injection. This is
probably done in order to make test driven development easier.

parseInt : JavaScript :: Integer.parseInt : Java. 

$resources is from the angular-resource.min.js file.

The $q service lets you start running computations and returns
promises. It's basically a synchronization library. It also
lets you avoid using call back functions.

$http is basically letting you do http requests, but in a fancier
way than XMLHTTPRequest.

$route is basically a thing for using resources from links
in other web pages. This probably means I didn't understand
it fully. Default route is provided with otherwise. Custom parameters
stay attached through navigation.

$location lets you access and modify the URL that you are at.

$log is basically a service for writing troubleshooting data.
Default implementation is console.log, but it would probably be
better to send a $POST request to your company's servers.
