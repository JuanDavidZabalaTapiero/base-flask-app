const { src, dest, watch, series } = require("gulp")
const sass = require("gulp-sass")(require("sass"));
const cleanCSS = require("gulp-clean-css");
const rename = require("gulp-rename");

// RUTAS
const paths = {
    scssAll: "scss/**/*.scss", // watcher: todos los scss
    scssNoPartials: ["scss/**/*.scss", "!scss/**/_*.scss"], // Compilar sin parciales
    cssOutput: "../app/static/css"
}

// COMPILAR Y MINIFICAR SCSS
function styles() {
    return src(paths.scssNoPartials, { base: "scss" }) // Base para mantener subcarpetas
        .pipe(sass().on("error", sass.logError))
        .pipe(cleanCSS())
        .pipe(rename({ suffix: ".min" }))
        .pipe(dest(paths.cssOutput));
}

// VIGILAR CAMBIOS
function watcher() {
    watch(paths.scssAll, styles)
}

// EXPORTAR TAREAS
exports.styles = styles;
exports.default = series(styles, watcher);