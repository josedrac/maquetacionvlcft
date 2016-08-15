// Include gulp
var gulp = require('gulp');

// Include Our Plugins
var autoprefixer    = require('gulp-autoprefixer'),
  concat            = require('gulp-concat'),
  del               = require('del'),
  jshint            = require('gulp-jshint'),
  minifycss         = require('gulp-minify-css'),
  notify            = require('gulp-notify'),
  path              = require('path'),
  runSequence       = require('run-sequence'),
  sass              = require('gulp-sass'),
  shell             = require('gulp-shell'),
  connect           = require('gulp-connect'),
  uglify            = require('gulp-uglify'),
  injectScripts     = require('gulp-angular-embed-templates');

var src_app         = './app',
  src_base_dir      = './app/assets',
  src_js_files      = [
    path.join(src_base_dir, 'js/plugins', '**', '*.js'),
    path.join(src_base_dir, 'js', '*.js')
  ],
  src_fonts_files   = path.join(src_base_dir, 'fonts', '**', '*'),
  src_sass_files    = path.join(src_base_dir, 'sass', '**', '*.scss'),

  dist_base_dir           = './app/dist',
  dist_js_dir             = path.join(dist_base_dir, 'js'),
  dist_css_dir            = path.join(dist_base_dir, 'css'),
  dist_font_dir           = path.join(dist_base_dir, 'fonts'),
  dist_font_dir_rob       = path.join(dist_font_dir, 'roboto'),
  dist_font_dir_bootstrap = path.join(dist_font_dir, 'bootstrap'),
  dist_html_dir           = path.join(src_app, 'templates'),
  src_html_files          = path.join(dist_html_dir, '**', '*.html'),
  src_py_files            = './context_vars/*.py',
  config_dir              = './config',

  vendor_js_src = [
    './bower_components/jquery/dist/jquery.min.js',
    './bower_components/bootstrap-sass/assets/javascripts/bootstrap.min.js',
    './bower_components/jQuery.mmenu/dist/js/jquery.mmenu.min.all.js',
    './bower_components/jquery-ui/jquery-ui.min.js',
    './bower_components/bootstrap-select/dist/js/bootstrap-select.min.js',
    './bower_components/modernizr/modernizr.js',
    './bower_components/wowjs/dist/wow.min.js'
  ],
  vendor_css_src = [
    './bower_components/font-awesome/css/font-awesome.min.css',
    './bower_components/bootstrap-select/dist/css/bootstrap-select.min.css',
    './bower_components/wowjs/css/libs/animate.css'
  ],
  vendor_source_maps = [
    './bower_components/jquery/dist/jquery.min.map',
  ];
  vendor_font_src = [
      './bower_components/font-awesome/fonts/*',
  ];
  vendor_font_src_roboto = [
      './bower_components/roboto-fontface/fonts/roboto/*',
  ];
  vendor_font_src_bootstrap = [
      './bower_components/bootstrap-sass/assets/fonts/bootstrap/*',
  ];

gulp.task('jshint', function() {
  return gulp.src(src_js_files)
    .pipe(jshint(path.join(config_dir, 'dev.jshintrc')))
    .pipe(jshint.reporter('jshint-stylish', {
      verbose: true
    }));
}).help = 'Analyzes js code quality with jshint according default config file.';


gulp.task('jshint-dist', function() {
  return gulp.src(src_js_files)
    .pipe(jshint(path.join(config_dir, 'dist.jshintrc')))
    .pipe(jshint.reporter('jshint-stylish'));
}).help = 'Analyzes js code quality with jshint according dist config file.';


gulp.task('sass', function() {
  return gulp.src(src_sass_files)
    .pipe(sass({
      errLogToConsole: true,
      outputStyle: 'expanded',
      sourceComments: true
    }))
    .pipe(autoprefixer({
      browsers: ['last 3 version', 'ie >= 10']
    }))
    .pipe(gulp.dest(dist_css_dir));
}).help = 'Compiles and autoprefixes sass source files.';


gulp.task('sass-min', function() {
  return gulp.src(src_sass_files)
    .pipe(sass({
      errLogToConsole: true,
      outputStyle: 'compressed',
      sourceComments: false
    }))
    .pipe(autoprefixer({
      browsers: ['last 3 version', 'ie >= 10']
    }))
    .pipe(minifycss())
    .pipe(gulp.dest(dist_css_dir));
}).help = 'Compiles, minifies and autoprefixes sass source files.';


gulp.task('vendor-css', function() {
  return gulp.src(vendor_css_src)
    .pipe(concat('vendor.css'))
    .pipe(gulp.dest(dist_css_dir));
}).help = 'Concatenates css vendor files.';

gulp.task('vendor-fonts', function() {
  return gulp.src(vendor_font_src)
    .pipe(gulp.dest(dist_font_dir));
}).help = 'Adds fonts vendor files.';

gulp.task('vendor-fonts-roboto', function() {
  return gulp.src(vendor_font_src_roboto)
    .pipe(gulp.dest(dist_font_dir_rob));
}).help = 'Adds fonts vendor files.';

gulp.task('vendor-font-bootstrap', function() {
  return gulp.src(vendor_font_src_bootstrap)
    .pipe(gulp.dest(dist_font_dir_bootstrap));
}).help = 'Adds fonts vendor files.';

gulp.task('scripts', function() {
  return gulp.src(src_js_files)
    .pipe(concat('app.js'))
    .pipe(gulp.dest(dist_js_dir));
}).help = 'Concatenates all js files.';


gulp.task('scripts-min', function() {
  return gulp.src(src_js_files)
    .pipe(concat('app.js'))
    .pipe(uglify())
    .pipe(gulp.dest(dist_js_dir));
}).help = 'Concatenates and minifies all js files.';

gulp.task('watch', function() {
  gulp.watch(src_js_files, ['jshint', 'scripts']);
  gulp.watch(src_sass_files, ['sass']);
  gulp.watch(src_html_files, ['jinja']);
   gulp.watch(src_py_files, ['jinja']);
}).help = 'Keeps watching for changes in sass (trigger jshint and scripts) and javascript (trigger sass).';

gulp.task('clean', function(cb) {
  del([dist_base_dir], cb);
}).help = 'Removes files in css and javascript destination folders.';


gulp.task('help', function() {
  ghelp.show();
}).help = 'Shows this help message.';


gulp.task('jinja', function() {
  return gulp.src('', {
      read: false
    })
    .pipe(shell(['python3 ./build.py']));
});

gulp.task('images', function() {
  return gulp.src(['app/assets/images/**/*']).pipe(gulp.dest('app/dist/images'));
});

gulp.task('fonts', function() {
  return gulp.src([src_fonts_files]).pipe(gulp.dest(dist_font_dir));
});

gulp.task('old_browsers', function() {
  return gulp.src(['app/assets/js/old_browsers_support/**/*']).pipe(gulp.dest('app/dist/js/old_browsers_support'));
});

gulp.task('inject-files',function() {
    gulp.src(vendor_js_src)
        .pipe(injectScripts())
        .pipe(gulp.dest(dist_js_dir));
});

gulp.task('connect', function() {
  return connect.server({
    root: './app/dist',
    port: 7000,
    livereload: false
  });
});

gulp.task('default', function() {
  runSequence(
    ['clean'],
    ['old_browsers', 'fonts', 'images', 'jshint', 'sass', 'vendor-css', 'vendor-fonts', 'vendor-fonts-roboto', 'vendor-font-bootstrap', 'scripts-min', 'inject-files', 'jinja'],
    ['watch', 'connect'],
    function() {
      gulp.src('').pipe(notify({
        title: 'Development',
        message: 'Built task done, now watching for changes...'
      }));
    }
  );
}).help = 'Build assets for development. Executes jshint, sass, vendor-scripts and scripts. Keeps watching for changes';
