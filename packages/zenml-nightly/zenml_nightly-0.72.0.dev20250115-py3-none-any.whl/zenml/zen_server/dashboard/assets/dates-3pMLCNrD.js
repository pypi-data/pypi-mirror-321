function c(t,n){if(!t||!n)return"Not available";const e=new Date(t),o=new Date(n);if(isNaN(e.getTime())||isNaN(o.getTime()))return"";const s=Math.abs(o.getTime()-e.getTime()),a=Math.floor(s/(1e3*60)),i=Math.floor(s%(1e3*60)/1e3);return`${a}min ${i}s`}function r(t){const n=new Date,e=new Date;return e.setMonth(n.getMonth()-6),t<e}function l(t){const n=new Date,e=new Date;return e.setFullYear(n.getFullYear()-1),t<e}export{l as a,c,r as i};
