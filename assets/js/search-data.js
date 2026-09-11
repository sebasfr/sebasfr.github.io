// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-about",
    title: "about",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-about",
          title: "about",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/";
          },
        },{id: "nav-research",
          title: "research",
          description: "A collection of my research and writing.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/research/";
          },
        },{id: "nav-cv",
          title: "cv",
          description: "Key takeaways from my CV. A PDF version is also available.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/cv/";
          },
        },{id: "nav-notes",
          title: "notes",
          description: "Class notes from courses I have taken, shared as-is.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/notes/";
          },
        },{id: "nav-teaching",
          title: "teaching",
          description: "Courses taught and teaching materials.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/teaching/";
          },
        },{id: "books-the-godfather",
          title: 'The Godfather',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/the_godfather/";
            },},{id: "courses-sequences",
          title: 'Sequences',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0350/01-sequences/";
            },},{id: "courses-subsequences",
          title: 'Subsequences',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0350/02-subsequences/";
            },},{id: "courses-limit-superior-and-limit-inferior",
          title: 'Limit Superior and Limit Inferior',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0350/03-limit-superior-and-inferior/";
            },},{id: "courses-numerical-series",
          title: 'Numerical Series',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0350/04-numerical-series/";
            },},{id: "courses-convergence-tests-for-series",
          title: 'Convergence Tests for Series',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0350/05-convergence-tests-for-series/";
            },},{id: "courses-the-riemann-integral",
          title: 'The Riemann Integral',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0350/06-the-riemann-integral/";
            },},{id: "courses-integration-techniques",
          title: 'Integration Techniques',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0350/07-integration-techniques/";
            },},{id: "courses-applications-of-the-riemann-integral",
          title: 'Applications of the Riemann Integral',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0350/08-applications-of-the-riemann-integral/";
            },},{id: "courses-improper-integrals",
          title: 'Improper Integrals',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0350/09-improper-integrals/";
            },},{id: "courses-series-of-functions",
          title: 'Series of Functions',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0350/10-series-of-functions/";
            },},{id: "courses-convergence-of-functions",
          title: 'Convergence of Functions',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0350/11-convergence-of-functions/";
            },},{id: "courses-important-topics-and-examples",
          title: 'Important Topics and Examples',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0350/12-important-topics-and-examples/";
            },},{id: "courses-single-variable-real-analysis",
          title: 'Single Variable Real Analysis',
          description: "Class notes from a one-semester course on the analysis of real-valued functions of a single real variable.",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0350/";
            },},{id: "courses-sucesiones",
          title: 'Sucesiones',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0350/es/01-sucesiones/";
            },},{id: "courses-subsucesiones",
          title: 'Subsucesiones',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0350/es/02-subsucesiones/";
            },},{id: "courses-límite-superior-e-inferior",
          title: 'Límite superior e inferior',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0350/es/03-limite-superior-e-inferior/";
            },},{id: "courses-series-numéricas",
          title: 'Series numéricas',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0350/es/04-series-numericas/";
            },},{id: "courses-criterios-de-convergencia-de-series",
          title: 'Criterios de convergencia de series',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0350/es/05-criterios-de-convergencia-de-series/";
            },},{id: "courses-integral-de-riemann",
          title: 'Integral de Riemann',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0350/es/06-integral-de-riemann/";
            },},{id: "courses-técnicas-de-integración",
          title: 'Técnicas de integración',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0350/es/07-tecnicas-de-integracion/";
            },},{id: "courses-aplicaciones-de-la-integral-de-riemann",
          title: 'Aplicaciones de la integral de Riemann',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0350/es/08-aplicaciones-de-la-integral-de-riemann/";
            },},{id: "courses-integrales-impropias",
          title: 'Integrales impropias',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0350/es/09-integrales-impropias/";
            },},{id: "courses-series-de-funciones",
          title: 'Series de funciones',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0350/es/10-series-de-funciones/";
            },},{id: "courses-convergencia-de-funciones",
          title: 'Convergencia de funciones',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0350/es/11-convergencia-de-funciones/";
            },},{id: "courses-tópicos-importantes-y-ejemplos",
          title: 'Tópicos importantes y ejemplos',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0350/es/12-topicos-importantes-y-ejemplos/";
            },},{id: "courses-cálculo-en-una-variable-2",
          title: 'Cálculo en una Variable 2',
          description: "Apuntes de un curso semestral sobre el análisis de funciones reales de una variable real.",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0350/es/";
            },},{id: "courses-topology-of-rn",
          title: 'Topology of Rn',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0450/01-topology-of-rn/";
            },},{id: "courses-functions-of-several-variables",
          title: 'Functions of Several Variables',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0450/02-functions-of-several-variables/";
            },},{id: "courses-differentiation",
          title: 'Differentiation',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0450/03-differentiation/";
            },},{id: "courses-integration-in-rn",
          title: 'Integration in Rn',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0450/04-integration-in-rn/";
            },},{id: "courses-vector-calculus",
          title: 'Vector Calculus',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0450/05-vector-calculus/";
            },},{id: "courses-multivariate-real-analysis",
          title: 'Multivariate Real Analysis',
          description: "Class notes from a one-semester course on real analysis in n dimensions, generalising single-variable analysis to several variables.",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0450/";
            },},{id: "courses-topología-en-rn",
          title: 'Topología en Rn',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0450/es/01-topologia-en-rn/";
            },},{id: "courses-funciones-de-varias-variables",
          title: 'Funciones de varias variables',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0450/es/02-funciones-de-varias-variables/";
            },},{id: "courses-diferenciación",
          title: 'Diferenciación',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0450/es/03-diferenciacion/";
            },},{id: "courses-integración-en-rn",
          title: 'Integración en Rn',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0450/es/04-integracion-en-rn/";
            },},{id: "courses-cálculo-vectorial",
          title: 'Cálculo vectorial',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0450/es/05-calculo-vectorial/";
            },},{id: "courses-cálculo-en-varias-variables",
          title: 'Cálculo en varias variables',
          description: "Apuntes de un curso semestral sobre el análisis real en n dimensiones, que generaliza el análisis de una variable a varias variables.",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0450/es/";
            },},{id: "courses-review-norms-on-rd-and-connectedness",
          title: 'Review: Norms on Rd and Connectedness',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0505/01-review-norms-on-rd-and-connectedness/";
            },},{id: "courses-metric-spaces",
          title: 'Metric Spaces',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0505/02-metric-spaces/";
            },},{id: "courses-basic-topological-properties",
          title: 'Basic Topological Properties',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0505/03-basic-topological-properties/";
            },},{id: "courses-continuity",
          title: 'Continuity',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0505/04-continuity/";
            },},{id: "courses-compactness",
          title: 'Compactness',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0505/05-compactness/";
            },},{id: "courses-completeness",
          title: 'Completeness',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0505/06-completeness/";
            },},{id: "courses-the-arzelà-ascoli-theorem",
          title: 'The Arzelà–Ascoli Theorem',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0505/07-the-arzela-ascoli-theorem/";
            },},{id: "courses-connectedness",
          title: 'Connectedness',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0505/08-connectedness/";
            },},{id: "courses-baire-categories",
          title: 'Baire Categories',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0505/09-baire-categories/";
            },},{id: "courses-functions-of-bounded-variation",
          title: 'Functions of Bounded Variation',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0505/10-functions-of-bounded-variation/";
            },},{id: "courses-the-riemann-stieltjes-integral",
          title: 'The Riemann–Stieltjes Integral',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0505/11-the-riemann-stieltjes-integral/";
            },},{id: "courses-outer-measure",
          title: 'Outer Measure',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0505/12-outer-measure/";
            },},{id: "courses-lebesgue-measure",
          title: 'Lebesgue Measure',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0505/13-lebesgue-measure/";
            },},{id: "courses-measurable-functions",
          title: 'Measurable Functions',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0505/14-measurable-functions/";
            },},{id: "courses-the-egorov-and-lusin-theorems",
          title: 'The Egorov and Lusin Theorems',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0505/15-the-egorov-and-lusin-theorems/";
            },},{id: "courses-convergence-in-measure",
          title: 'Convergence in Measure',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0505/16-convergence-in-measure/";
            },},{id: "courses-the-lebesgue-integral-of-non-negative-functions",
          title: 'The Lebesgue Integral of Non-negative Functions',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0505/17-the-lebesgue-integral-of-non-negative-functions/";
            },},{id: "courses-properties-of-the-integral-of-non-negative-functions",
          title: 'Properties of the Integral of Non-negative Functions',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0505/18-properties-of-the-integral-of-non-negative-functions/";
            },},{id: "courses-the-lebesgue-integral-of-measurable-functions",
          title: 'The Lebesgue Integral of Measurable Functions',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0505/19-the-lebesgue-integral-of-measurable-functions/";
            },},{id: "courses-the-relationship-between-the-riemann-and-lebesgue-integrals",
          title: 'The Relationship Between the Riemann and Lebesgue Integrals',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0505/20-the-relationship-between-the-riemann-and-lebesgue-integrals/";
            },},{id: "courses-metric-spaces-and-measure-theory",
          title: 'Metric Spaces and Measure Theory',
          description: "Class notes from a one-semester course on metric space topology and the Lebesgue theory of measure and integration.",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0505/";
            },},{id: "courses-repaso-normas-en-rd-y-conexidad",
          title: 'Repaso: normas en Rd y conexidad',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0505/es/01-repaso-normas-en-rd-y-conexidad/";
            },},{id: "courses-espacios-métricos",
          title: 'Espacios métricos',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0505/es/02-espacios-metricos/";
            },},{id: "courses-propiedades-topológicas-básicas",
          title: 'Propiedades topológicas básicas',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0505/es/03-propiedades-topologicas-basicas/";
            },},{id: "courses-continuidad",
          title: 'Continuidad',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0505/es/04-continuidad/";
            },},{id: "courses-compacidad",
          title: 'Compacidad',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0505/es/05-compacidad/";
            },},{id: "courses-completitud",
          title: 'Completitud',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0505/es/06-completitud/";
            },},{id: "courses-el-teorema-de-arzelà-ascoli",
          title: 'El Teorema de Arzelà-Ascoli',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0505/es/07-el-teorema-de-arzela-ascoli/";
            },},{id: "courses-conexidad",
          title: 'Conexidad',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0505/es/08-conexidad/";
            },},{id: "courses-categorías-de-baire",
          title: 'Categorías de Baire',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0505/es/09-categorias-de-baire/";
            },},{id: "courses-funciones-de-variación-acotada",
          title: 'Funciones de variación acotada',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0505/es/10-funciones-de-variacion-acotada/";
            },},{id: "courses-la-integral-de-riemann-stieltjes",
          title: 'La integral de Riemann–Stieltjes',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0505/es/11-la-integral-de-riemann-stieltjes/";
            },},{id: "courses-la-medida-exterior",
          title: 'La medida exterior',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0505/es/12-la-medida-exterior/";
            },},{id: "courses-la-medida-de-lebesgue",
          title: 'La medida de Lebesgue',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0505/es/13-la-medida-de-lebesgue/";
            },},{id: "courses-funciones-medibles",
          title: 'Funciones medibles',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0505/es/14-funciones-medibles/";
            },},{id: "courses-los-teoremas-de-egorov-y-lusin",
          title: 'Los teoremas de Egorov y Lusin',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0505/es/15-los-teoremas-de-egorov-y-lusin/";
            },},{id: "courses-convergencia-en-medida",
          title: 'Convergencia en medida',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0505/es/16-convergencia-en-medida/";
            },},{id: "courses-la-integral-de-lebesgue-de-funciones-no-negativas",
          title: 'La integral de Lebesgue de funciones no negativas',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0505/es/17-la-integral-de-lebesgue-de-funciones-no-negativas/";
            },},{id: "courses-propiedades-de-la-integral-de-funciones-no-negativas",
          title: 'Propiedades de la integral de funciones no negativas',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0505/es/18-propiedades-de-la-integral-de-funciones-no-negativas/";
            },},{id: "courses-la-integral-de-lebesgue-de-funciones-medibles",
          title: 'La integral de Lebesgue de funciones medibles',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0505/es/19-la-integral-de-lebesgue-de-funciones-medibles/";
            },},{id: "courses-la-relación-entre-las-integrales-de-riemann-y-lebesgue",
          title: 'La relación entre las integrales de Riemann y Lebesgue',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0505/es/20-la-relacion-entre-las-integrales-de-riemann-y-lebesgue/";
            },},{id: "courses-análisis-i",
          title: 'Análisis I',
          description: "Apuntes de un curso semestral sobre la topología de los espacios métricos y la teoría de la medida y la integral de Lebesgue.",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0505/es/";
            },},{id: "courses-groups-subgroups-and-centralizers",
          title: 'Groups, Subgroups and Centralizers',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0561/01-groups-subgroups-and-centralizers/";
            },},{id: "courses-cyclic-groups-and-their-subgroups",
          title: 'Cyclic Groups and Their Subgroups',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0561/02-cyclic-groups-and-their-subgroups/";
            },},{id: "courses-the-permutation-group",
          title: 'The Permutation Group',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0561/03-the-permutation-group/";
            },},{id: "courses-group-homomorphisms",
          title: 'Group Homomorphisms',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0561/04-group-homomorphisms/";
            },},{id: "courses-chain-complexes-and-exact-sequences",
          title: 'Chain Complexes and Exact Sequences',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0561/05-chain-complexes-and-exact-sequences/";
            },},{id: "courses-translation-and-conjugation",
          title: 'Translation and Conjugation',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0561/06-translation-and-conjugation/";
            },},{id: "courses-cosets",
          title: 'Cosets',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0561/07-cosets/";
            },},{id: "courses-normal-subgroups",
          title: 'Normal Subgroups',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0561/08-normal-subgroups/";
            },},{id: "courses-the-quotient-group",
          title: 'The Quotient Group',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0561/09-the-quotient-group/";
            },},{id: "courses-the-isomorphism-theorems",
          title: 'The Isomorphism Theorems',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0561/10-the-isomorphism-theorems/";
            },},{id: "courses-group-actions",
          title: 'Group Actions',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0561/11-group-actions/";
            },},{id: "courses-orbits-and-stabilizers",
          title: 'Orbits and Stabilizers',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0561/12-orbits-and-stabilizers/";
            },},{id: "courses-simple-groups",
          title: 'Simple Groups',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0561/13-simple-groups/";
            },},{id: "courses-the-sylow-theorems",
          title: 'The Sylow Theorems',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0561/14-the-sylow-theorems/";
            },},{id: "courses-rings",
          title: 'Rings',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0561/15-rings/";
            },},{id: "courses-the-polynomial-ring",
          title: 'The Polynomial Ring',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0561/16-the-polynomial-ring/";
            },},{id: "courses-ideals",
          title: 'Ideals',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0561/17-ideals/";
            },},{id: "courses-prime-ideals",
          title: 'Prime Ideals',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0561/18-prime-ideals/";
            },},{id: "courses-products-of-rings",
          title: 'Products of Rings',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0561/19-products-of-rings/";
            },},{id: "courses-quotient-rings",
          title: 'Quotient Rings',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0561/20-quotient-rings/";
            },},{id: "courses-ring-homomorphisms",
          title: 'Ring Homomorphisms',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0561/21-ring-homomorphisms/";
            },},{id: "courses-prime-subrings-and-characteristic",
          title: 'Prime Subrings and Characteristic',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0561/22-prime-subrings-and-characteristic/";
            },},{id: "courses-the-field-of-fractions",
          title: 'The Field of Fractions',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0561/23-the-field-of-fractions/";
            },},{id: "courses-factorization-of-homomorphisms",
          title: 'Factorization of Homomorphisms',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0561/24-factorization-of-homomorphisms/";
            },},{id: "courses-groups-and-rings",
          title: 'Groups and Rings',
          description: "Class notes from a one-semester first course in abstract algebra, covering group theory and then ring theory.",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0561/";
            },},{id: "courses-grupos-subgrupos-y-centralizadores",
          title: 'Grupos, subgrupos y centralizadores',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0561/es/01-grupos-subgrupos-y-centralizadores/";
            },},{id: "courses-grupos-cíclicos-y-sus-subgrupos",
          title: 'Grupos cíclicos y sus subgrupos',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0561/es/02-grupos-ciclicos-y-sus-subgrupos/";
            },},{id: "courses-grupo-de-permutaciones",
          title: 'Grupo de permutaciones',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0561/es/03-grupo-de-permutaciones/";
            },},{id: "courses-homomorfismos-de-grupos",
          title: 'Homomorfismos de grupos',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0561/es/04-homomorfismos-de-grupos/";
            },},{id: "courses-cadenas-y-sucesiones-exactas",
          title: 'Cadenas y sucesiones exactas',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0561/es/05-cadenas-y-sucesiones-exactas/";
            },},{id: "courses-traslación-y-conjugación",
          title: 'Traslación y conjugación',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0561/es/06-traslacion-y-conjugacion/";
            },},{id: "courses-coclases",
          title: 'Coclases',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0561/es/07-coclases/";
            },},{id: "courses-subgrupos-normales",
          title: 'Subgrupos normales',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0561/es/08-subgrupos-normales/";
            },},{id: "courses-grupo-cociente",
          title: 'Grupo cociente',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0561/es/09-grupo-cociente/";
            },},{id: "courses-teoremas-del-isomorfismo",
          title: 'Teoremas del isomorfismo',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0561/es/10-teoremas-del-isomorfismo/";
            },},{id: "courses-acciones-de-grupo",
          title: 'Acciones de grupo',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0561/es/11-acciones-de-grupo/";
            },},{id: "courses-órbitas-y-estabilizadores",
          title: 'Órbitas y estabilizadores',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0561/es/12-orbitas-y-estabilizadores/";
            },},{id: "courses-grupos-simples",
          title: 'Grupos simples',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0561/es/13-grupos-simples/";
            },},{id: "courses-teoremas-de-sylow",
          title: 'Teoremas de Sylow',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0561/es/14-teoremas-de-sylow/";
            },},{id: "courses-anillos",
          title: 'Anillos',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0561/es/15-anillos/";
            },},{id: "courses-el-anillo-de-polinomios",
          title: 'El anillo de polinomios',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0561/es/16-el-anillo-de-polinomios/";
            },},{id: "courses-ideales",
          title: 'Ideales',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0561/es/17-ideales/";
            },},{id: "courses-ideales-primos",
          title: 'Ideales primos',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0561/es/18-ideales-primos/";
            },},{id: "courses-productos-de-anillos",
          title: 'Productos de anillos',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0561/es/19-productos-de-anillos/";
            },},{id: "courses-anillos-cociente",
          title: 'Anillos cociente',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0561/es/20-anillos-cociente/";
            },},{id: "courses-homomorfismos-de-anillos",
          title: 'Homomorfismos de anillos',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0561/es/21-homomorfismos-de-anillos/";
            },},{id: "courses-subanillos-primos-y-característica",
          title: 'Subanillos primos y característica',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0561/es/22-subanillos-primos-y-caracteristica/";
            },},{id: "courses-el-cuerpo-de-fracciones",
          title: 'El cuerpo de fracciones',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0561/es/23-el-cuerpo-de-fracciones/";
            },},{id: "courses-factorización-de-homomorfismos",
          title: 'Factorización de homomorfismos',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0561/es/24-factorizacion-de-homomorfismos/";
            },},{id: "courses-grupos-y-anillos",
          title: 'Grupos y Anillos',
          description: "Apuntes de un primer curso semestral de álgebra abstracta, que cubre la teoría de grupos y luego la teoría de anillos.",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0561/es/";
            },},{id: "news-launching-my-personal-academic-website",
          title: 'Launching my personal academic website',
          description: "",
          section: "News",handler: () => {
              window.location.href = "/news/2026-01-12-welcome/";
            },},{id: "news-new-working-paper-out-the-gap-between-mandate-and-execution-an-evaluation-of-the-inflation-target-in-costa-rica-finds-empirical-evidence-supporting-the-existence-of-a-contractionary-bias-in-costa-rica-s-monetary-policy-read-it-on-my-research-page",
          title: 'New working paper out! “The Gap Between Mandate and Execution: An Evaluation of...',
          description: "",
          section: "News",},{id: "news-class-notes-published-single-and-multivariate-real-analysis",
          title: 'Class notes published — Single and Multivariate Real Analysis',
          description: "",
          section: "News",handler: () => {
              window.location.href = "/news/2026-04-28-course-notes/";
            },},{id: "news-two-more-sets-of-class-notes-analysis-i-and-groups-and-rings",
          title: 'Two more sets of class notes — Analysis I and Groups and Rings...',
          description: "",
          section: "News",handler: () => {
              window.location.href = "/news/2026-09-10-algebra-and-analysis-notes/";
            },},{id: "projects-project-1",
          title: 'project 1',
          description: "with background image",
          section: "Projects",handler: () => {
              window.location.href = "/projects/1_project/";
            },},{id: "projects-project-2",
          title: 'project 2',
          description: "a project with a background image and giscus comments",
          section: "Projects",handler: () => {
              window.location.href = "/projects/2_project/";
            },},{id: "projects-project-3-with-very-long-name",
          title: 'project 3 with very long name',
          description: "a project that redirects to another website",
          section: "Projects",handler: () => {
              window.location.href = "/projects/3_project/";
            },},{id: "projects-project-4",
          title: 'project 4',
          description: "another without an image",
          section: "Projects",handler: () => {
              window.location.href = "/projects/4_project/";
            },},{id: "projects-project-5",
          title: 'project 5',
          description: "a project with a background image",
          section: "Projects",handler: () => {
              window.location.href = "/projects/5_project/";
            },},{id: "projects-project-6",
          title: 'project 6',
          description: "a project with no image",
          section: "Projects",handler: () => {
              window.location.href = "/projects/6_project/";
            },},{id: "projects-project-7",
          title: 'project 7',
          description: "with background image",
          section: "Projects",handler: () => {
              window.location.href = "/projects/7_project/";
            },},{id: "projects-project-8",
          title: 'project 8',
          description: "an other project with a background image and giscus comments",
          section: "Projects",handler: () => {
              window.location.href = "/projects/8_project/";
            },},{id: "projects-project-9",
          title: 'project 9',
          description: "another project with an image 🎉",
          section: "Projects",handler: () => {
              window.location.href = "/projects/9_project/";
            },},{
        id: 'social-email',
        title: 'email',
        section: 'Socials',
        handler: () => {
          window.open("mailto:%73%65%62%61%73%74%69%61%6E.%66%65%72%6E%61%6E%64%65%7A%72%69%76%65%72%61%32%34@%67%6D%61%69%6C.%63%6F%6D", "_blank");
        },
      },{
        id: 'social-linkedin',
        title: 'LinkedIn',
        section: 'Socials',
        handler: () => {
          window.open("https://www.linkedin.com/in/sebasfr", "_blank");
        },
      },{
        id: 'social-github',
        title: 'GitHub',
        section: 'Socials',
        handler: () => {
          window.open("https://github.com/sebasfr", "_blank");
        },
      },{
      id: 'light-theme',
      title: 'Change theme to light',
      description: 'Change the theme of the site to Light',
      section: 'Theme',
      handler: () => {
        setThemeSetting("light");
      },
    },
    {
      id: 'dark-theme',
      title: 'Change theme to dark',
      description: 'Change the theme of the site to Dark',
      section: 'Theme',
      handler: () => {
        setThemeSetting("dark");
      },
    },
    {
      id: 'system-theme',
      title: 'Use system default theme',
      description: 'Change the theme of the site to System Default',
      section: 'Theme',
      handler: () => {
        setThemeSetting("system");
      },
    },];
