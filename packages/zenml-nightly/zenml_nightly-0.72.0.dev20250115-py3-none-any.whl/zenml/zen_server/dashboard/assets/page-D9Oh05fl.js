import{j as e,r as m}from"./@radix-DeK6qiuw.js";import{av as g,aw as b,ax as v,ay as y,az as S,B as h,aA as C}from"./index-CE0aQlv8.js";import{I as l}from"./Infobox-Da6-76M2.js";import{V as d,g as p}from"./Commands-BEGyld4c.js";import{H as j}from"./Helpbox-Bb1ed--O.js";import{S as w,a as k,b as A}from"./gcp-CFtm4BA7.js";import{S as z}from"./kubernetes-B2wmAJ1d.js";import{S as T}from"./docker-BdA9vrnW.js";import"./@tanstack-DT5WLu9C.js";import"./@react-router-B3Z5rLr2.js";import"./@reactflow-BUNIMFeC.js";import"./CodeSnippet-DIJRT2NT.js";import"./copy-C8XQA2Ug.js";import"./help-Cc9bBIJH.js";const N="/assets/connectors-video-C9qY4syJ.svg",s="w-5 h-5",P=[{label:"Kubernetes",value:"kubernetes",icon:e.jsx(z,{className:s})},{label:"GCP",value:"gcp",icon:e.jsx(w,{className:s})},{label:"Docker",value:"docker",icon:e.jsx(T,{className:s})},{label:"Azure",value:"azure",icon:e.jsx(k,{className:s})},{label:"AWS",value:"aws",icon:e.jsx(A,{className:s})}],I={help:{href:"https://docs.zenml.io/how-to/infrastructure-deployment/auth-management/kubernetes-service-connector",text:"Use the complete guide to set up your Kubernetes Service Connector."},prerequisites:i("kubernetes","Kubernetes"),listCommand:a("kubernetes","Kubernetes"),topInfobox:"The ZenML Kubernetes service connector facilitates authenticating and connecting to a Kubernetes cluster. The connector can be used to access to any generic Kubernetes cluster by providing pre-authenticated Kubernetes python clients to Stack Components that are linked to it and also allows configuring the local Kubernetes CLI (i.e. kubectl).",bottomInfobox:"Upon completion of the installation of the required prerequisites and integration, our documentation provides you with a comprehensive list of resource types that can be employed to establish your connector. Please refer to the documentation to explore all available options."},q={help:{text:"Use the complete guide to set up your GCP Service Connector.",href:"https://docs.zenml.io/how-to/infrastructure-deployment/auth-management/gcp-service-connector"},prerequisites:i("gcp","GCP"),listCommand:a("gcp","GCP"),bottomInfobox:"Upon completion of the installation of the required prerequisites and integration, our documentation will guide you with a comprehensive list of all the resource types that can be employed to establish your GCP connector. Please refer to the documentation to explore all available options.",topInfobox:"The ZenML GCP Service Connector facilitates the authentication and access to managed GCP services and resources. These encompass a range of resources, including GCS buckets, GCR container repositories, and GKE clusters. The connector provides support for various authentication methods, including GCP user accounts, service accounts, short-lived OAuth 2.0 tokens, and implicit authentication."},G={help:{text:"Use the complete guide to set up your Docker Service Connector.",href:"https://docs.zenml.io/how-to/infrastructure-deployment/auth-management/docker-service-connector"},listCommand:a("docker","Docker"),topInfobox:"The ZenML Docker Service Connector allows authenticating with a Docker or OCI container registry and managing Docker clients for the registry. This connector provides pre-authenticated python-docker Python clients to Stack Components that are linked to it.",bottomInfobox:"No Python packages are required for this Service Connector. All prerequisites are included in the base ZenML Python package. Docker needs to be installed on environments where container images are built and pushed to the target container registry. Please refer to the documentation to explore all available options."},K={help:{text:"Use the complete guide to set up your Azure Service Connector.",href:"https://docs.zenml.io/how-to/infrastructure-deployment/auth-management/azure-service-connector"},listCommand:a("azure","Azure"),prerequisites:i("azure","Azure"),topInfobox:"The ZenML Azure Service Connector facilitates the authentication and access to managed Azure services and resources. These encompass a range of resources, including blob storage containers, ACR repositories, and AKS clusters.",bottomInfobox:"Upon completion of the installation of the required prerequisites and integration, our documentation will guide you with a comprehensive list of all the resource types that can be employed to establish your Azure connector. Please refer to the documentation to explore all available options."},L={help:{text:"Use the complete guide to set up your AWS Service Connector.",href:"https://docs.zenml.io/how-to/infrastructure-deployment/auth-management/aws-service-connector"},listCommand:a("aws","AWS"),prerequisites:i("aws","AWS"),topInfobox:"The ZenML AWS Service Connector facilitates the authentication and access to managed AWS services and resources. These encompass a range of resources, including S3 buckets, ECR container repositories, and EKS clusters. The connector provides support for various authentication methods, including explicit long-lived AWS secret keys, IAM roles, short-lived STS tokens, and implicit authentication.",bottomInfobox:"Upon completion of the installation of the required prerequisites and integration, our documentation will guide you with a comprehensive list of all the resource types that can be employed to establish your AWS connector. Please refer to the documentation to explore all available options."};function a(t,o){return{command:`zenml service-connector list-types --type ${t}`,description:`List ${o} Connector Types`}}function i(t,o){return[{description:"Install the prerequisites",command:`pip install "zenml[connectors-${t}]"`},{description:`Install the entire ${o} ZenML integration`,command:`zenml integration install ${t}`}]}function M({id:t,selectedType:o,onTypeChange:c}){return e.jsxs(g,{value:o,onValueChange:n=>c(n),children:[e.jsx(b,{id:t,className:"w-[250px] border border-neutral-300 px-2 text-left text-text-md",children:e.jsx(v,{placeholder:"Select Connector Type"})}),e.jsx(y,{className:"",children:P.map(n=>e.jsx(S,{value:n.value,children:e.jsxs("div",{className:"flex items-center gap-1",children:[n.icon,n.label]})},n.value))})]})}function W(){return e.jsx(l,{children:e.jsxs("div",{className:"flex w-full flex-wrap items-center gap-x-2 gap-y-0.5 text-text-md",children:[e.jsx("p",{className:"font-semibold",children:"We are creating a new Connectors experience"}),e.jsx("p",{children:"In the meanwhile you can use the CLI to add and manage your connectors."})]})})}function D(){const t="https://zenml.portal.trainn.co/share/V6magMJZZvMptz1wdnUmPA/embed?autoplay=false";return e.jsxs(h,{className:"flex flex-col-reverse items-stretch overflow-hidden lg:flex-row",children:[e.jsxs("div",{className:"w-full p-7 lg:w-2/3",children:[e.jsx("h2",{className:"text-display-xs font-semibold",children:"Learn More about Connectors"}),e.jsx("p",{className:"mt-2 text-text-lg text-theme-text-secondary",children:"Dive into Service Connector Types for a documented approach to secure authentication and authorization practices."}),e.jsx(d,{videoLink:t,buttonText:"Watch the Starter Guide (2 min)"})]}),e.jsx("div",{className:"flex w-full items-center justify-center bg-primary-50 lg:w-1/3",children:e.jsx(d,{fallbackImage:e.jsx("img",{src:N,alt:"Purple squares with text indicating a starter guide for secrets",className:"h-full w-full"}),videoLink:t,isButton:!1})})]})}function U(){const[t,o]=m.useState("kubernetes");return e.jsxs("section",{className:"space-y-5 pl-8 pr-5",children:[e.jsx(M,{selectedType:t,onTypeChange:o,id:"connector-select"}),Z(t)]})}function r({topInfobox:t,bottomInfobox:o,listCommand:c,prerequisites:n,help:u}){return e.jsxs(e.Fragment,{children:[e.jsx(l,{className:"text-text-md",intent:"neutral",children:t}),p(c),n&&e.jsxs(e.Fragment,{children:[e.jsx("p",{children:"Prerequisites"}),n.map((x,f)=>e.jsx(m.Fragment,{children:p(x)},f))]}),e.jsx(l,{className:"text-text-md",intent:"neutral",children:o}),e.jsx(j,{text:u.text,link:u.href})]})}function Z(t){switch(t){case"kubernetes":return r(I);case"gcp":return r(q);case"docker":return r(G);case"azure":return r(K);case"aws":return r(L)}}function te(){return e.jsxs(h,{className:"space-y-4 p-5",children:[e.jsx("h1",{className:"text-text-xl font-semibold",children:"Secrets"}),e.jsx(W,{}),e.jsx(D,{}),e.jsxs("div",{className:"flex items-center gap-2",children:[e.jsx(C,{}),"Administering your Connectors"]}),e.jsx(U,{})]})}export{te as default};
