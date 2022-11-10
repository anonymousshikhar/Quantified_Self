# healthify

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### In case running the project on wsl 2.0, add the following statement to webpack.json file
```
html : {template : './public/index.ejs'}
```
* This uses Embedded Javascript Templating engine in order to render the index.html file, which in turns solve the problem of HMR (Hot Module Reload) often faced while using wsl 2.0 
