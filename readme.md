
# Installation

1. To install dependencies, assuming that you already have installed node, npm and ruby at least.

   Check what gems are installed with `gem list` should be, at least,

      sass (3.4.13)  
      scss-lint (0.37.0)

   if not, install or update sass and scss-lint

   Check if bower is available with `bower -v` if it is missing, install it

   globally with `npm install -g bower`

   Check if gulp is available with `gulp -v` if it is missing, install it

   globally with `npm install -g gulp`


2. To install project

   You need to run: `npm install`


3. Gulp: `gulp [task] [option]`
    * The default `[task]`, build the project on dist folder in app directory of the project and run the APP on localhost.

        > You can add a `[option]` `--uglify` to minimize css and uglify js code.

    * The build `[task]`, build the project on dist folder in app directory of the project.

        > You can add a `[option]` `--uglify` to minimize css and uglify js code.

        > You can add a `[option]` `--release` to build in a release folder and upload on a repository a release with the settings inserted on terminal.

4. Notes:

    * The script of the Google's captcha can't be downloaded, and it's been added from google's servers (as Google says). Also it must include the public key on the page domain.

# Useful links

1. Resources

  * [HTML5 W3C Reference] (http://dev.w3.org/html5/html-author)
  * [HTML5 MDN guide] (https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) and [tags reference] (https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5/HTML5_element_list)
  * [SASS] (http://sass-lang.com/guide) language reference.
  * [CSS Guide Lines] (http://cssguidelin.es) is **the main guidelines to follow in the project to successfully complete it in a sane, manageable and scalable way**.
  * [BEM notation] (https://bem.info/method/definitions) applyed to css naming, but it must be used [carefully] (http://csswizardry.com/2013/01/mindbemding-getting-your-head-round-bem-syntax)
  * [OOCSS] (http://appendto.com/2014/04/oocss) introduction
  * [Javascript patterns] (http://shichuan.github.io/javascript-patterns)

2. Gulp plugins

  * [child_process] (https://nodejs.org/api/child_process.html)
  * [autoprefixer] (https://www.npmjs.org/package/gulp-autoprefixer/)
  * [concat] (https://www.npmjs.org/package/gulp-concat/)
  * [connect] (https://www.npmjs.com/package/gulp-connect/)
  * [github-release] (https://www.npmjs.com/package/gulp-github-release/)
  * [gulp-htmlhint] (https://www.npmjs.com/package/gulp-htmlhint/)
  * [del] (https://www.npmjs.org/package/del/)
  * [if] (https://github.com/robrich/gulp-if/)
  * [jshint] (https://www.npmjs.org/package/gulp-jshint/)
  * [minifycss] (https://www.npmjs.org/package/gulp-minify-css/)
  * [notify] (https://www.npmjs.org/package/gulp-notify/)
  * [prompt] (https://www.npmjs.com/package/gulp-prompt)
  * [htmlhint-stylish] (https://www.npmjs.com/package/htmlhint-stylish/)
  * [jshint-stylish] (https://www.npmjs.com/package/jshint-stylish/)
  * [runSequence] (https://www.npmjs.org/package/run-sequence/)
  * [sass] (https://www.npmjs.org/package/gulp-sass/)
  * [uglify] (https://www.npmjs.org/package/gulp-uglify/)
  * [zip] (https://www.npmjs.com/package/gulp-zip/)

3. Font Icons

  * [icomoon] (https://icomoon.io/app/#/select)

    > Font Name: FontMercadona

    > Class Prefix: icon-fmd-

    > Support IE 8 checked

    > CSS Selector: Use Attribute Selectors

    > Font Metrics 1024; 6.25; 50;

    > Version 1.0

	### Object fit module

	Module used: [object-fit-images](https://github.com/bfred-it/object-fit-images)

	Once installed, import `<script src="js/ofi.browser.js"></script>`

	The [author mixin](https://github.com/bfred-it/object-fit-images/blob/gh-pages/preprocessors/mixin.scss) is imported in `mixins.scss`

	Usage: `@include object-fit(cover);`

	And finally, in the `document.ready` event: `window.objectFitImages();`

	### Linters

	The **linters** used in the project are:

	* Linter Html [(atom plugin)](https://atom.io/packages/linter-htmlhint)

	* Linter Jscs [(atom plugin)](https://atom.io/packages/linter-jscs)

	* Linter Jshint [(atom plugin)](https://atom.io/packages/linter-jshint)

	* Linter Scss [(atom plugin)](https://atom.io/packages/linter-scss-lint)

	*Each linter has his own configuration file. See instructions in the plugin page for more details.*
https://www.sitepoint.com/getting-started-with-scss-lint/
	apm install linter-scss-lint
	Installing linter-scss-lint to /Users/josedrac/.atom/packages ✓
	apm install linter-jshint
	Installing linter-jshint to /Users/josedrac/.atom/packages ✓
	apm install linter-jscs
	Installing linter-jscs to /Users/josedrac/.atom/packages ✓
	apm install linter-htmlhint
	Installing linter-htmlhint to /Users/josedrac/.atom/packages ✓
	apm install atom-beautify
	Installing atom-beautify to /Users/josedrac/.atom/packages
