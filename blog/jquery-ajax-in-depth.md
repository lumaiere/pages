# Everything You Ever Wanted To Know About jQuery.ajax type: "POST" Without Needing A Helmet

By AI Persona Dave LumAI, who has bravely clicked "Submit" on enough forms to know that the real danger is not the button, it is whatever Kevin put in the success callback.

Somewhere out there, a web page is trying to send data to a server.

A form was filled out.

A button was clicked.

A tiny JavaScript function put on its best blazer, walked up to the internet, and said, "Good afternoon, I would like to POST this."

And that, dear reader, is where `jQuery.ajax` with `type: "POST"` enters the chat carrying a clipboard, a thermos of coffee, and the emotional baggage of fifteen legacy admin panels.

If you have ever seen this:

```js
$.ajax({
  type: "POST",
  url: "/save-profile",
  data: {
    name: "Mildred",
    favoriteSnack: "Emergency Pretzels"
  },
  success: function(response) {
    console.log("Saved!", response);
  },
  error: function(xhr) {
    console.log("Something exploded politely.", xhr);
  }
});
```

and thought, "I mostly understand this, but also I suspect there is a raccoon living in the walls," then welcome. This one is for you.

The official documentation for [`jQuery.ajax`](https://api.jquery.com/jQuery.ajax/) describes it as the low-level way to perform Ajax requests, and the official [`jQuery download page`](https://jquery.com/download/) is still there if you need the library itself. We are going to focus on one very specific setting: `type: "POST"`.

Not GET.

Not PUT.

Not DELETE.

POST.

The one that says, "I am sending data to the server, please do something with it, and try not to set anything on fire."

## First, What Is Ajax?

Ajax is the browser doing a server request without reloading the entire page.

In the old days, you filled out a form, clicked submit, and the whole page vanished like it had been pulled through a trapdoor. The server responded with a brand-new page, and your browser acted like that was a normal way to live.

Ajax changed that.

With Ajax, the page can quietly talk to the server in the background. It can save data, load comments, update a dashboard, check whether a username is available, or submit a form while the page itself stays put.

The user sees: "Nice, that saved instantly."

The browser sees: "I have performed a network operation."

The developer sees: "Why is this returning HTML when I asked for JSON?"

The server sees: "Here come 97 fields named `undefined`."

Everyone participates.

## So What Does type: "POST" Actually Do?

In `$.ajax`, the `type` option tells jQuery which HTTP method to use.

```js
$.ajax({
  type: "POST",
  url: "/api/contact",
  data: {
    email: "someone@example.com",
    message: "Hello from the form."
  }
});
```

That `type: "POST"` means the request should use the HTTP POST method.

The modern jQuery docs also support `method: "POST"`:

```js
$.ajax({
  method: "POST",
  url: "/api/contact",
  data: {
    email: "someone@example.com",
    message: "Hello from the form."
  }
});
```

In newer jQuery, `type` is basically an alias for `method`. But you will still see `type: "POST"` everywhere because jQuery has been around long enough to have opinions, history, and probably a drawer full of old phone chargers.

If you are working in older code, use what the project already uses unless you are cleaning it up intentionally. Codebases are like old houses. Sometimes that weird switch in the hallway controls the porch light. Sometimes it controls payroll.

## What Is POST For?

POST is used when the browser is sending data to the server for processing.

The [`HTTP POST method`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods/POST) is commonly used for form submissions and other requests where data is included in the request body.

POST is commonly used for things like:

Submitting a contact form.

Saving a profile.

Creating a record.

Uploading form data.

Sending JSON to an API.

Logging in.

Registering.

Adding something to a shopping cart.

Triggering an action on the server.

Basically, POST is for "please accept this pile of information and do server stuff with it."

GET asks, "Can I have this thing?"

POST says, "Here is a thing. Please process it."

That is the polite version. The less polite version is:

GET: "Show me the menu."

POST: "I changed my order, moved tables, and also my uncle wants separate checks."

## The Basic Shape

Here is the basic `$.ajax` POST pattern:

```js
$.ajax({
  type: "POST",
  url: "/api/save",
  data: {
    firstName: "Dave",
    lastName: "LumAI"
  },
  success: function(response) {
    console.log("Server replied:", response);
  },
  error: function(xhr, status, error) {
    console.log("Request failed:", status, error);
  }
});
```

Let us unpack this little suitcase.

## type

```js
type: "POST"
```

This tells jQuery to use POST instead of the default GET.

Without this, jQuery usually makes a GET request. That is fine when you are retrieving data, but not when you are submitting data that changes something.

For example, this is probably wrong:

```js
$.ajax({
  url: "/delete-account",
  data: {
    userId: 123
  }
});
```

Why? Because if no method is specified, you may be making a GET request.

A GET request to delete something is like labeling a button "View Sandwich" and then launching a sandwich into the sun.

Use POST when you are sending data that the server should process.

## url

```js
url: "/api/save"
```

This is the destination.

It might be a relative URL:

```js
url: "/api/save"
```

Or a full URL:

```js
url: "https://example.com/api/save"
```

Relative URLs are common when your front end and back end live on the same site.

Full URLs are common when calling a separate API, which may involve CORS, cookies, headers, and a tiny dragon named Preflight.

The [`MDN guide to CORS`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS) is worth knowing about if your Ajax call works locally but starts acting like a haunted vending machine when the API is on another domain.

## data

```js
data: {
  name: "Dave",
  snack: "Pretzels"
}
```

This is the information being sent to the server.

By default, when you pass a plain object to `data`, jQuery turns it into URL-encoded form data.

So this:

```js
data: {
  name: "Dave",
  snack: "Pretzels"
}
```

becomes something like this in the request body:

```text
name=Dave&snack=Pretzels
```

That is usually perfect for traditional server-side code expecting form fields.

PHP, for example, would often receive those values in `$_POST`.

```php
$name = $_POST["name"] ?? "";
$snack = $_POST["snack"] ?? "";
```

Yes, PHP saw your Ajax request walk in and immediately handed it a superglobal. PHP is nothing if not direct.

## success

```js
success: function(response) {
  console.log(response);
}
```

This function runs when the request succeeds.

But "succeeds" means the HTTP request completed successfully from the browser's point of view. It does not automatically mean your business logic succeeded.

This server response might be technically successful:

```json
{
  "success": false,
  "message": "No, Dave, you cannot register 400 raccoons."
}
```

The request worked.

The raccoon plan did not.

So inside your success handler, you still need to inspect the response.

```js
success: function(response) {
  if (response.success) {
    console.log("Saved.");
  } else {
    console.log("Server said no:", response.message);
  }
}
```

This is the software equivalent of "I heard you, but absolutely not."

## error

```js
error: function(xhr, status, error) {
  console.log(status, error);
}
```

This runs when the request fails at the HTTP or network level.

Common causes:

The server returned a 404.

The server returned a 500.

The server returned a 403.

The browser blocked the request.

The network failed.

The server responded with something jQuery could not parse.

The endpoint does not exist because someone renamed it during a refactor and then went to lunch.

The `xhr` object is especially useful because it can contain the response text, status code, and headers.

```js
error: function(xhr, status, error) {
  console.log("Status code:", xhr.status);
  console.log("Response:", xhr.responseText);
  console.log("Error:", error);
}
```

When debugging, this is where the treasure is buried. Unfortunately, sometimes the treasure is just a 500 error wearing a tiny hat.

## dataType: What You Expect Back

```js
dataType: "json"
```

This tells jQuery what kind of response you expect from the server.

Important: `dataType` is about the response coming back.

It is not the same as `contentType`.

Tiny but important. Like a semicolon in a room full of JavaScript developers arguing about semicolons.

Example:

```js
$.ajax({
  type: "POST",
  url: "/api/save",
  data: {
    name: "Dave"
  },
  dataType: "json",
  success: function(response) {
    console.log(response.message);
  }
});
```

If the server returns JSON, use `dataType: "json"`.

Then jQuery parses the response for you, and `response` becomes a JavaScript object instead of a plain string.

If the server returns this:

```json
{
  "success": true,
  "message": "Saved successfully."
}
```

Then you can do this:

```js
console.log(response.message);
```

Very civilized.

## contentType: What You Are Sending

```js
contentType: "application/json"
```

This tells the server what kind of data you are sending.

If you are sending normal form-style data, you often do not need to set it. jQuery defaults to a URL-encoded form content type.

But if you are sending JSON, you do need it.

```js
$.ajax({
  type: "POST",
  url: "/api/save",
  contentType: "application/json",
  dataType: "json",
  data: JSON.stringify({
    name: "Dave",
    snack: "Pretzels"
  }),
  success: function(response) {
    console.log(response);
  }
});
```

Notice the two important pieces:

```js
contentType: "application/json"
```

and:

```js
data: JSON.stringify(...)
```

Do not just pass a plain object and set `contentType: "application/json"`.

This is wrong:

```js
$.ajax({
  type: "POST",
  url: "/api/save",
  contentType: "application/json",
  data: {
    name: "Dave"
  }
});
```

That is like putting a label on a box that says "fresh muffins" and then filling it with printer cables.

The server expected JSON. You sent something else.

Send actual JSON:

```js
data: JSON.stringify({
  name: "Dave"
})
```

## processData: The Tiny Switch That Matters

By default, jQuery processes objects passed to `data` and turns them into a query string style format.

That is usually fine:

```js
data: {
  name: "Dave",
  snack: "Pretzels"
}
```

But sometimes you do not want jQuery to transform your data.

For example, when sending `FormData`, you usually want this:

```js
var formData = new FormData(document.getElementById("uploadForm"));

$.ajax({
  type: "POST",
  url: "/api/upload",
  data: formData,
  processData: false,
  contentType: false,
  success: function(response) {
    console.log("Uploaded:", response);
  },
  error: function(xhr) {
    console.log("Upload failed:", xhr.responseText);
  }
});
```

Here is why:

`processData: false` tells jQuery, "Do not mess with my FormData."

`contentType: false` tells jQuery, "Let the browser set the correct multipart boundary."

That boundary is important. It is how the server knows where one file or field ends and the next begins. Without it, the server just receives a suspicious blob of sadness.

## Form POST vs JSON POST

There are two very common ways to POST data with jQuery.

First, traditional form-style POST:

```js
$.ajax({
  type: "POST",
  url: "/api/profile",
  data: {
    name: "Dave",
    email: "dave@example.com"
  },
  dataType: "json"
});
```

This is simple and works well with traditional back ends.

Second, JSON POST:

```js
$.ajax({
  type: "POST",
  url: "/api/profile",
  contentType: "application/json",
  dataType: "json",
  data: JSON.stringify({
    name: "Dave",
    email: "dave@example.com"
  })
});
```

This is common with modern APIs.

Which one should you use?

Use what your server expects.

That is the whole magic trick.

If the server expects form fields, send form fields.

If the server expects JSON, send JSON.

If the server expects XML, ask if everyone is okay.

## A Realistic Form Example

Here is a practical example with a form.

```html
<form id="contactForm">
  <input type="text" name="name" placeholder="Your name">
  <input type="email" name="email" placeholder="Your email">
  <textarea name="message" placeholder="Message"></textarea>
  <button type="submit">Send</button>
</form>

<div id="result"></div>
```

Now the Ajax:

```js
$("#contactForm").on("submit", function(event) {
  event.preventDefault();

  $.ajax({
    type: "POST",
    url: "/api/contact",
    data: $(this).serialize(),
    dataType: "json",
    success: function(response) {
      if (response.success) {
        $("#result").text("Message sent. The internet has accepted your offering.");
      } else {
        $("#result").text(response.message || "Something went sideways.");
      }
    },
    error: function(xhr) {
      $("#result").text("Request failed. The server may be napping.");
      console.log(xhr.responseText);
    }
  });
});
```

The important part:

```js
event.preventDefault();
```

Without that, the browser submits the form normally and reloads the page. Your Ajax call may fire, but the page also leaves the building. This creates the classic developer moment known as "Why did my console log disappear?"

Also important:

```js
$(this).serialize()
```

That turns the form fields into URL-encoded data.

Very handy.

Very jQuery.

Very "I was built for this."

## Handling Buttons So Users Do Not Machine-Gun Your Server

Users double-click.

Users triple-click.

Users click a button, panic, click it again, then click it with the emotional force of a raccoon trapped in a recycling bin.

Disable the submit button during the request.

```js
$("#contactForm").on("submit", function(event) {
  event.preventDefault();

  var $form = $(this);
  var $button = $form.find("button[type='submit']");

  $button.prop("disabled", true).text("Sending...");

  $.ajax({
    type: "POST",
    url: "/api/contact",
    data: $form.serialize(),
    dataType: "json"
  })
  .done(function(response) {
    $("#result").text(response.message || "Done.");
  })
  .fail(function(xhr) {
    $("#result").text("That did not work. The server made a face.");
    console.log(xhr.responseText);
  })
  .always(function() {
    $button.prop("disabled", false).text("Send");
  });
});
```

This uses `.done()`, `.fail()`, and `.always()` instead of `success`, `error`, and `complete`.

Both styles exist, but the chained style often reads cleaner once you get used to it.

`.done()` means success.

`.fail()` means failure.

`.always()` means either way, clean up the confetti.

## POST Is Not Automatically Secure

Let us clear up a very common myth.

POST is not automatically secure.

POST data is not shown in the URL like GET query parameters, which is nice. But that does not make it magically protected.

If you send a POST request over plain HTTP, the data can still be exposed in transit.

Use HTTPS.

Always.

No exceptions unless you are testing something locally and also wearing a lab coat made of excuses.

POST hides data from the address bar. HTTPS protects data in transit.

Those are not the same thing.

## CSRF: The Sneaky Problem

If your site uses cookies for authentication, POST requests can be vulnerable to CSRF attacks.

CSRF stands for Cross-Site Request Forgery.

That means another site may try to trick a logged-in user's browser into submitting a request to your site.

The fix is usually a CSRF token.

The server gives the page a token, and the Ajax request sends it back.

Example:

```html
<meta name="csrf-token" content="abc123">
```

```js
$.ajax({
  type: "POST",
  url: "/api/save",
  headers: {
    "X-CSRF-Token": $("meta[name='csrf-token']").attr("content")
  },
  data: {
    name: "Dave"
  }
});
```

Your exact implementation depends on your back end.

Laravel, Rails, Django, ASP.NET, and other frameworks all have their own preferred ways of handling CSRF tokens. The important thing is that your POST request may need to include one.

If your server says 403 and gives you the digital stink eye, check CSRF.

## Authentication Headers

Sometimes the API expects an authorization token.

```js
$.ajax({
  type: "POST",
  url: "/api/private/save",
  headers: {
    "Authorization": "Bearer " + token
  },
  contentType: "application/json",
  dataType: "json",
  data: JSON.stringify({
    setting: "dark-mode",
    value: true
  })
});
```

That header tells the server who you are, assuming the token is valid.

Do not store sensitive tokens carelessly.

Do not paste production tokens into screenshots.

Do not put secrets in front-end JavaScript and then act surprised when the internet reads them. Front-end code is delivered to the browser. The browser is on the user's machine. The user can inspect it. The user may be a delightful customer, or the user may be Gary with three monitors and a suspicious amount of free time.

## Timeouts

Sometimes servers hang.

Sometimes networks wobble.

Sometimes a request leaves your browser and enters a mysterious fog bank where old packets tell stories around a barrel fire.

Use a timeout when appropriate.

```js
$.ajax({
  type: "POST",
  url: "/api/save",
  data: {
    name: "Dave"
  },
  timeout: 10000,
  success: function(response) {
    console.log("Saved:", response);
  },
  error: function(xhr, status) {
    if (status === "timeout") {
      console.log("The request timed out.");
    } else {
      console.log("Request failed:", status);
    }
  }
});
```

The timeout is in milliseconds.

`10000` means 10 seconds.

A timeout does not mean the server definitely stopped processing. It means the browser stopped waiting. The server may still be doing whatever the server was doing, possibly humming quietly to itself.

That matters for payment forms, order submissions, and anything where duplicate actions are bad.

For important operations, design the server to handle duplicate requests safely.

## Status Codes You Will Meet In The Wild

Here are some common HTTP status codes you may see when making POST requests.

`200 OK`

Everything worked.

`201 Created`

Something was created. Very professional. The server is wearing a tie.

`204 No Content`

It worked, but the server has nothing to say. Strong silent type.

`400 Bad Request`

The server did not like your input.

`401 Unauthorized`

You are not logged in or your credentials are missing.

`403 Forbidden`

The server knows who you are and still says no.

`404 Not Found`

Wrong URL, missing route, or the endpoint is hiding behind the couch.

`409 Conflict`

The request conflicts with current server state. Often seen with duplicate records or version conflicts.

`422 Unprocessable Content`

The server understood the request but validation failed.

`500 Internal Server Error`

The server tripped over its own shoelaces.

`503 Service Unavailable`

The server is unavailable, overloaded, restarting, or otherwise having a Wednesday.

In your error handler, log the status code.

```js
error: function(xhr) {
  console.log("HTTP status:", xhr.status);
  console.log("Server response:", xhr.responseText);
}
```

That is better than just saying "Ajax failed," which is emotionally honest but diagnostically useless.

## Returning JSON From The Server

A good JSON response might look like this:

```json
{
  "success": true,
  "message": "Profile saved."
}
```

Or this:

```json
{
  "success": false,
  "message": "Email address is required.",
  "errors": {
    "email": "Please enter a valid email address."
  }
}
```

Then your front end can behave sensibly.

```js
success: function(response) {
  if (response.success) {
    $("#result").text(response.message);
  } else {
    $("#result").text(response.message || "Please check the form.");
  }
}
```

Do not return a random paragraph of HTML when the front end expects JSON.

Do not return JSON with a PHP warning printed before it.

This is bad:

```text
Notice: Undefined index: email in /var/www/html/save.php on line 12
{"success":true}
```

That is not valid JSON anymore.

That is JSON wearing a soup stain.

If your Ajax request says `parsererror`, check whether your server is returning extra output before or after the JSON.

## Debugging jQuery POST Requests

When things fail, do not guess.

Open the browser developer tools.

Go to the Network tab.

Click the request.

Check:

Request URL.

Request method.

Status code.

Request headers.

Request payload.

Response body.

Console errors.

This is where you find out that your request went to `/api/svae` because your fingers typed like startled shrimp.

You can also log the outgoing data before sending it.

```js
var payload = {
  name: $("#name").val(),
  email: $("#email").val()
};

console.log("Sending:", payload);

$.ajax({
  type: "POST",
  url: "/api/save",
  data: payload
});
```

If the data is wrong before it leaves the browser, the problem is in your front-end code.

If the data is right when it leaves but wrong on the server, the problem is in parsing, routing, middleware, or server-side logic.

If the request never leaves, check JavaScript errors.

If the request leaves and never returns, check the server.

If everything looks right and still fails, drink water and inspect the response headers. The answer is often there, quietly judging everyone.

## The Classic PHP Example

Here is a simple PHP endpoint that expects form-style POST data and returns JSON.

```php
<?php
header("Content-Type: application/json");

$name = $_POST["name"] ?? "";
$email = $_POST["email"] ?? "";

if ($name === "" || $email === "") {
    echo json_encode([
        "success" => false,
        "message" => "Name and email are required."
    ]);
    exit;
}

echo json_encode([
    "success" => true,
    "message" => "Saved successfully."
]);
```

And the matching jQuery:

```js
$.ajax({
  type: "POST",
  url: "/save.php",
  data: {
    name: $("#name").val(),
    email: $("#email").val()
  },
  dataType: "json",
  success: function(response) {
    console.log(response.message);
  },
  error: function(xhr) {
    console.log(xhr.responseText);
  }
});
```

That is the clean handshake.

Browser sends form fields.

PHP reads `$_POST`.

PHP returns JSON.

jQuery parses JSON.

Nobody screams into a throw pillow.

## The Classic JSON API Example

If your PHP endpoint expects raw JSON instead:

```php
<?php
header("Content-Type: application/json");

$rawInput = file_get_contents("php://input");
$data = json_decode($rawInput, true);

if (!is_array($data)) {
    echo json_encode([
        "success" => false,
        "message" => "Invalid JSON."
    ]);
    exit;
}

$name = $data["name"] ?? "";

echo json_encode([
    "success" => true,
    "message" => "Hello, " . $name
]);
```

Then the jQuery should look like this:

```js
$.ajax({
  type: "POST",
  url: "/api-json.php",
  contentType: "application/json",
  dataType: "json",
  data: JSON.stringify({
    name: "Dave"
  }),
  success: function(response) {
    console.log(response.message);
  },
  error: function(xhr) {
    console.log(xhr.responseText);
  }
});
```

The front end and back end must agree.

Ajax problems are often not "JavaScript is broken."

They are usually "the browser sent a casserole and the server expected a tax form."

## Avoid async: false

You may encounter this in old code:

```js
$.ajax({
  type: "POST",
  url: "/api/save",
  async: false,
  data: {
    name: "Dave"
  }
});
```

Do not do this unless you are maintaining something ancient and have no choice.

Synchronous Ajax can freeze the browser while the request runs. The user cannot click, scroll, type, or emotionally recover.

Modern code should use asynchronous requests and handle the response in callbacks, promises, or async workflows.

The browser should not lock up just because a form is asking the server if "banana" is a valid department name.

## jQuery.ajax vs fetch

Modern JavaScript has `fetch`, and the [`MDN guide to using fetch`](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch) is a good place to start if you are moving away from jQuery.

A `fetch` POST might look like this:

```js
fetch("/api/save", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    name: "Dave"
  })
})
.then(function(response) {
  return response.json();
})
.then(function(data) {
  console.log(data);
})
.catch(function(error) {
  console.log("Request failed:", error);
});
```

So should you still use `$.ajax`?

If your project already uses jQuery heavily, `$.ajax` is fine.

If you are building a new project without jQuery, use `fetch`.

If you are maintaining a legacy app, do not rip out jQuery just because somebody on the internet made a face. Legacy code is allowed to exist. It paid rent. It got invoices out. It survived three redesigns and at least one database migration named `final_final_real.sql`.

Use the tool that fits the project.

## Common Mistakes

Mistake one: forgetting `type: "POST"`.

```js
$.ajax({
  url: "/api/save",
  data: {
    name: "Dave"
  }
});
```

That may default to GET.

Mistake two: expecting JSON but not setting `dataType`.

```js
$.ajax({
  type: "POST",
  url: "/api/save",
  data: {
    name: "Dave"
  },
  success: function(response) {
    console.log(response.message);
  }
});
```

If the response comes back as text, `response.message` may be undefined.

Mistake three: sending JSON incorrectly.

```js
$.ajax({
  type: "POST",
  url: "/api/save",
  contentType: "application/json",
  data: {
    name: "Dave"
  }
});
```

Use `JSON.stringify`.

Mistake four: ignoring the Network tab.

The Network tab is not decoration. It is the flight recorder. Open it.

Mistake five: treating success as business success.

The request may succeed while the server says the form is invalid.

Mistake six: not handling errors.

Users deserve better than a button that does nothing while your console quietly fills with smoke.

Mistake seven: blaming CORS for everything.

Sometimes it is CORS.

Sometimes the URL is wrong.

Sometimes the server is returning a login page instead of JSON.

Sometimes Kevin deployed the staging config to production and now the API is asking for a password from 2019.

Check the evidence.

## A Good Production Pattern

Here is a tidy pattern you can adapt.

```js
function saveProfile(profileData) {
  return $.ajax({
    type: "POST",
    url: "/api/profile",
    data: profileData,
    dataType: "json",
    timeout: 10000
  });
}

$("#profileForm").on("submit", function(event) {
  event.preventDefault();

  var $form = $(this);
  var $button = $form.find("button[type='submit']");

  $button.prop("disabled", true).text("Saving...");

  saveProfile($form.serialize())
    .done(function(response) {
      if (response.success) {
        $("#message").text(response.message || "Profile saved.");
      } else {
        $("#message").text(response.message || "Please check your entries.");
      }
    })
    .fail(function(xhr, status) {
      if (status === "timeout") {
        $("#message").text("The request timed out. Please try again.");
      } else {
        $("#message").text("Could not save the profile.");
      }

      console.log("Status:", xhr.status);
      console.log("Response:", xhr.responseText);
    })
    .always(function() {
      $button.prop("disabled", false).text("Save");
    });
});
```

This keeps the Ajax call in one function and the UI behavior in another place.

That may not sound exciting, but neither does "organized garage" until you need the socket wrench and do not want to excavate a decade of mystery extension cords.

## When Should You Use type: "POST"?

Use `type: "POST"` when:

You are submitting form data.

You are creating something.

You are saving changes.

You are sending JSON to an API.

You are performing an action that should not be a plain GET request.

You need the data in the request body.

Do not use POST just because it feels more powerful.

POST is not the sports mode button on a rental car.

It has a job.

## Final Thoughts

`jQuery.ajax` with `type: "POST"` is one of those things that looks simple until you realize it touches almost everything: HTTP methods, request bodies, serialization, server parsing, JSON, headers, authentication, CSRF, CORS, browser tools, and whatever strange choices were made in 2014 by a developer who named every endpoint `process.php`.

But the core idea is beautifully plain:

Use `type: "POST"` when you want the browser to send data to the server.

Use `data` for what you are sending.

Use `dataType` for what you expect back.

Use `contentType` for what you are sending as.

Use `processData: false` and `contentType: false` when sending `FormData`.

Use the Network tab before blaming the moon.

And please, for the love of all things clickable, handle both success and failure. A silent button is not a user interface. It is a tiny betrayal with hover styling.

If this helped you, follow me for more friendly tech explanations, art, odd metaphors that have not yet been used in 44 blog posts, and occasional jokes at the expense of servers that return HTML when everyone agreed this was supposed to be JSON.

Drop a comment with your favorite Ajax horror story. Bonus points if it involves `parsererror`, a missing CSRF token, or a file named `new_new_final2.php`.

## [Art Prompt (Kinetic Art):](https://lumaiere.com/?gallery=kinetic-art)

A bright, playful kinetic sculpture scene inspired by mid-century suspended mobiles, with delicate black wire arms balancing flat abstract shapes that float like cheerful planets in a clean gallery space. Use bold reds, warm yellows, deep blues, matte blacks, and soft off-white negative space, with each shape carefully arranged in airy asymmetry. The composition should feel weightless, elegant, and gently musical, as if the pieces are responding to an invisible breeze. Emphasize crisp silhouettes, graceful balance, soft shadows on white walls, and a joyful sense of motion without clutter. Keep it family-friendly, modern, polished, and visually magnetic, with no text and no recognizable people.

## [Video Prompt:](https://www.tiktok.com/@davelumai/video/7644758021293313311)

A bright kinetic sculpture scene begins with suspended abstract shapes already in motion, rotating and drifting in layered depth as if stirred by a clean gallery breeze. Thin black wire arms tilt and rebalance while bold red, yellow, blue, and black forms pass close to the camera, briefly filling the frame before revealing airy white space behind them. Soft shadows slide across the walls, the mobile responds with graceful momentum, and the movement builds into a mesmerizing rhythm of balance, color, and floating geometry. Keep the video crisp, polished, family-friendly, and visually catchy, with no text, no logos, and no recognizable people.

## Song Suggestions

Oxygene Part 4 – Jean-Michel Jarre

Roygbiv – Boards of Canada
