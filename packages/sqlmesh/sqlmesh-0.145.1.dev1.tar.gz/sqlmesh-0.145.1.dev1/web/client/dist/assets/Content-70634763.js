import{d as a,Q as l,v as e,j as r,U as n,e as d}from"./index-176b79a9.js";import{D as u}from"./ReportErrors-64911a07.js";import"./PlusCircleIcon-2799ca1f.js";import"./transition-19ed7834.js";import"./_commonjs-dynamic-modules-302442b1.js";import"./SplitPane-94158256.js";function j(){const{errors:i}=a(),{id:s}=l(),o=e(s)?void 0:Array.from(i).find(t=>t.id===s);return r.jsx("div",{className:"flex overflow-auto w-full h-full",children:e(o)?r.jsx(n,{link:d.Errors,description:e(s)?void 0:`Error ${s} Does Not Exist`,message:"Back To Errors"}):r.jsx("div",{className:"p-4 h-full w-full",children:r.jsx("div",{className:"w-full h-full p-4 rounded-lg bg-danger-5 text-danger-700",children:r.jsx(u,{error:o,scope:o.key,withSplitPane:!0})})})})}export{j as default};
