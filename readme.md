
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


3. Gulp: default task

    * To run app: gulp   
    * To generate the static files: gulp dist

   Default task include the following tasks 'sass-lint', 'jshint', 'sass', 'vendor-scripts', 'scripts' and 'watch'.


# Useful links

1. Resources

  * [HTML5 W3C Reference] (http://dev.w3.org/html5/html-author)
  * [HTML5 MDN guide] (https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) and [tags reference] (https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5/HTML5_element_list)
  * [SASS] (http://sass-lang.com/guide) language reference.
  * [CSS Guide Lines] (http://cssguidelin.es) is **the main guidelines to follow in the project to successfully complete it in a sane, manageable and scalable way**.
  * [BEM notation] (https://bem.info/method/definitions) applyed to css naming, but it must be used [carefully] (http://csswizardry.com/2013/01/mindbemding-getting-your-head-round-bem-syntax)
  * [OOCSS] (http://appendto.com/2014/04/oocss) introduction
  * [Javascript patterns] (http://shichuan.github.io/javascript-patterns)

3. Gulp plugins

  * [autoprefixer] (https://www.npmjs.org/package/gulp-autoprefixer/)
  * [cache] (https://www.npmjs.org/package/gulp-cache/)
  * [concat] (https://www.npmjs.org/package/gulp-concat/)
  * [del] (https://www.npmjs.org/package/del/)
  * [jshint] (https://www.npmjs.org/package/gulp-jshint/)
  * [minifycss] (https://www.npmjs.org/package/gulp-minify-css/)
  * [notify] (https://www.npmjs.org/package/gulp-notify/)
  * [rename] (https://www.npmjs.org/package/gulp-rename/)
  * [runSequence] (https://www.npmjs.org/package/run-sequence/)
  * [sass] (https://www.npmjs.org/package/gulp-sass/)
  * [uglify] (https://www.npmjs.org/package/gulp-uglify/)
