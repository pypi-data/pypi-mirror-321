import{p as r,q as n,k as a,s as o,F as u}from"./index-CE0aQlv8.js";import{a as i}from"./@tanstack-DT5WLu9C.js";import{o as c}from"./url-Dh93fvh0.js";function p({params:e}){return["runs",e]}async function l({params:e}){const s=r(n.runs.all+"?"+c(e)),t=await a(s,{method:"GET",headers:{"Content-Type":"application/json"}});if(t.status===404&&o(),!t.ok)throw new u({message:"Error while fetching pipeline runs",status:t.status,statusText:t.statusText});return t.json()}function y(e,s){return i({queryKey:p(e),queryFn:()=>l(e),...s})}export{y as u};
