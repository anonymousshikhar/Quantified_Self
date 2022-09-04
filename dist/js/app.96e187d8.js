(function(){"use strict";var t={7398:function(t,n,r){var e=r(9242),a=r(3396);function o(t,n,r,e,o,s){const l=(0,a.up)("NavBar"),c=(0,a.up)("TableComponent"),i=(0,a.up)("HelloWorld");return(0,a.wg)(),(0,a.iD)(a.HY,null,[(0,a.Wm)(l),(0,a.Wm)(c),(0,a.Wm)(i)],64)}var s=r(7139);const l=t=>((0,a.dD)("data-v-2abbe872"),t=t(),(0,a.Cn)(),t),c={class:"container mt-5"},i=l((()=>(0,a._)("h3",null,"Tracker Records",-1)));function d(t,n,r,e,o,l){return(0,a.wg)(),(0,a.iD)("div",c,[i,(0,a._)("ul",null,[(0,a._)("li",null,(0,s.zw)(o.records[0].Tracker_name),1),(0,a._)("li",null,(0,s.zw)(o.records[0].Tracker_id),1)])])}var u={name:"HelloWorld",data(){return{records:[]}},methods:{getRecords(){fetch("http://127.0.0.1:8080/dashboard",{method:"GET",headers:{"Content-Type":"application/json"}}).then((t=>t.json())).then((t=>this.records.push(t))).catch((t=>console.log(t)))}},created(){this.getRecords()}},p=r(89);const h=(0,p.Z)(u,[["render",d],["__scopeId","data-v-2abbe872"]]);var f=h;const v={class:"navbar navbar-expand-lg navbar-light bg-light"},b=(0,a._)("a",{class:"navbar-brand",href:"#"},"Navbar",-1),m=(0,a._)("button",{class:"navbar-toggler",type:"button","data-toggle":"collapse","data-target":"#navbarSupportedContent","aria-controls":"navbarSupportedContent","aria-expanded":"false","aria-label":"Toggle navigation"},[(0,a._)("span",{class:"navbar-toggler-icon"})],-1),g={class:"collapse navbar-collapse justify-content-between",id:"navbarSupportedContent"},_={class:"navbar-nav mr-auto"},w=(0,a._)("li",{class:"nav-item active"},[(0,a._)("a",{class:"nav-link",href:"#"},[(0,a.Uk)("Home "),(0,a._)("span",{class:"sr-only"},"(current)")])],-1),y={class:"nav-item"},k=(0,a._)("li",{class:"nav-item dropdown"},[(0,a._)("a",{class:"nav-link dropdown-toggle",href:"#",id:"navbarDropdown",role:"button","data-toggle":"dropdown","aria-haspopup":"true","aria-expanded":"false"}," Dropdown "),(0,a._)("div",{class:"dropdown-menu","aria-labelledby":"navbarDropdown"},[(0,a._)("a",{class:"dropdown-item",href:"#"},"Action"),(0,a._)("a",{class:"dropdown-item",href:"#"},"Another action"),(0,a._)("div",{class:"dropdown-divider"}),(0,a._)("a",{class:"dropdown-item",href:"#"},"Something else here")])],-1),O=(0,a._)("li",{class:"nav-item"},[(0,a._)("a",{class:"nav-link disabled"},"Disabled")],-1),T=(0,a._)("form",{class:"form-inline"},[(0,a._)("input",{class:"form-control mr-sm-2",type:"search",placeholder:"Search","aria-label":"Search"}),(0,a._)("button",{class:"btn btn-outline-success my-2 my-sm-0",type:"submit"},"Search")],-1);function C(t,n,r,e,o,s){return(0,a.wg)(),(0,a.iD)("nav",v,[b,m,(0,a._)("div",g,[(0,a._)("ul",_,[w,(0,a._)("li",y,[(0,a._)("a",{class:"nav-link",onClick:n[0]||(n[0]=t=>s.func()),href:"#"},"Link")]),k,O]),T])])}var j={name:"NavBar",methods:{func(){fetch("http://127.0.0.1:8080/done").then((t=>t.text())).then((t=>console.log(t)))}}};const D=(0,p.Z)(j,[["render",C]]);var x=D;const S={class:"container mt-5"},H=(0,a.uE)('<table class="table"><thead class="thead-dark"><tr><th scope="col">#</th><th scope="col">First</th><th scope="col">Last</th><th scope="col">Handle</th></tr></thead><tbody><tr><th scope="row">1</th><td>Mark</td><td>Otto</td><td>@mdo</td></tr><tr><th scope="row">2</th><td>Jacob</td><td>Thornton</td><td>@fat</td></tr><tr><th scope="row">3</th><td>Larry</td><td>the Bird</td><td>@twitter</td></tr></tbody></table>',1),W=[H];function B(t,n,r,e,o,s){return(0,a.wg)(),(0,a.iD)("div",S,W)}var N={name:"TableComponent"};const Z=(0,p.Z)(N,[["render",B]]);var A=Z,E={name:"App",components:{HelloWorld:f,NavBar:x,TableComponent:A}};const L=(0,p.Z)(E,[["render",o]]);var R=L;(0,e.ri)(R).mount("#app")}},n={};function r(e){var a=n[e];if(void 0!==a)return a.exports;var o=n[e]={exports:{}};return t[e](o,o.exports,r),o.exports}r.m=t,function(){var t=[];r.O=function(n,e,a,o){if(!e){var s=1/0;for(d=0;d<t.length;d++){e=t[d][0],a=t[d][1],o=t[d][2];for(var l=!0,c=0;c<e.length;c++)(!1&o||s>=o)&&Object.keys(r.O).every((function(t){return r.O[t](e[c])}))?e.splice(c--,1):(l=!1,o<s&&(s=o));if(l){t.splice(d--,1);var i=a();void 0!==i&&(n=i)}}return n}o=o||0;for(var d=t.length;d>0&&t[d-1][2]>o;d--)t[d]=t[d-1];t[d]=[e,a,o]}}(),function(){r.n=function(t){var n=t&&t.__esModule?function(){return t["default"]}:function(){return t};return r.d(n,{a:n}),n}}(),function(){r.d=function(t,n){for(var e in n)r.o(n,e)&&!r.o(t,e)&&Object.defineProperty(t,e,{enumerable:!0,get:n[e]})}}(),function(){r.g=function(){if("object"===typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(t){if("object"===typeof window)return window}}()}(),function(){r.o=function(t,n){return Object.prototype.hasOwnProperty.call(t,n)}}(),function(){var t={143:0};r.O.j=function(n){return 0===t[n]};var n=function(n,e){var a,o,s=e[0],l=e[1],c=e[2],i=0;if(s.some((function(n){return 0!==t[n]}))){for(a in l)r.o(l,a)&&(r.m[a]=l[a]);if(c)var d=c(r)}for(n&&n(e);i<s.length;i++)o=s[i],r.o(t,o)&&t[o]&&t[o][0](),t[o]=0;return r.O(d)},e=self["webpackChunkfrontend"]=self["webpackChunkfrontend"]||[];e.forEach(n.bind(null,0)),e.push=n.bind(null,e.push.bind(e))}();var e=r.O(void 0,[998],(function(){return r(7398)}));e=r.O(e)})();
//# sourceMappingURL=app.96e187d8.js.map