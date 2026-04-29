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
            },},{id: "courses-single-variable-real-analysis",
          title: 'Single Variable Real Analysis',
          description: "Class notes from a one-semester course on the analysis of real-valued functions of a single real variable.",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0350/";
            },},{id: "courses-sucesiones",
          title: 'Sucesiones',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0350/01-sucesiones/";
            },},{id: "courses-subsucesiones",
          title: 'Subsucesiones',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0350/02-subsucesiones/";
            },},{id: "courses-límite-superior-e-inferior",
          title: 'Límite superior e inferior',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0350/03-limite-superior-e-inferior/";
            },},{id: "courses-series-numéricas",
          title: 'Series numéricas',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0350/04-series-numericas/";
            },},{id: "courses-criterios-de-convergencia-de-series",
          title: 'Criterios de convergencia de series',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0350/05-criterios-de-convergencia-de-series/";
            },},{id: "courses-integral-de-riemann",
          title: 'Integral de Riemann',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0350/06-integral-de-riemann/";
            },},{id: "courses-técnicas-de-integración",
          title: 'Técnicas de integración',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0350/07-tecnicas-de-integracion/";
            },},{id: "courses-aplicaciones-de-la-integral-de-riemann",
          title: 'Aplicaciones de la integral de Riemann',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0350/08-aplicaciones-de-la-integral-de-riemann/";
            },},{id: "courses-integrales-impropias",
          title: 'Integrales impropias',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0350/09-integrales-impropias/";
            },},{id: "courses-series-de-funciones",
          title: 'Series de funciones',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0350/10-series-de-funciones/";
            },},{id: "courses-convergencia-de-funciones",
          title: 'Convergencia de funciones',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0350/11-convergencia-de-funciones/";
            },},{id: "courses-tópicos-importantes-y-ejemplos",
          title: 'Tópicos importantes y ejemplos',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0350/12-topicos-importantes-y-ejemplos/";
            },},{id: "courses-multivariate-real-analysis",
          title: 'Multivariate Real Analysis',
          description: "Class notes from a one-semester course on real analysis in $\mathbb{R}^n$, generalising single-variable analysis to several variables.",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0450/";
            },},{id: "courses-topología-en-rn",
          title: 'Topología en Rn',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0450/01-topologia-en-rn/";
            },},{id: "courses-funciones-de-varias-variables",
          title: 'Funciones de varias variables',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0450/02-funciones-de-varias-variables/";
            },},{id: "courses-diferenciación",
          title: 'Diferenciación',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0450/03-diferenciacion/";
            },},{id: "courses-integración-en-rn",
          title: 'Integración en Rn',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0450/04-integracion-en-rn/";
            },},{id: "courses-cálculo-vectorial",
          title: 'Cálculo vectorial',
          description: "",
          section: "Courses",handler: () => {
              window.location.href = "/notes/ma0450/05-calculo-vectorial/";
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
