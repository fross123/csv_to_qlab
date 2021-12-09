// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

const lightCodeTheme = require('prism-react-renderer/themes/github');
const darkCodeTheme = require('prism-react-renderer/themes/dracula');

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'CSV to QLab',
  tagline: 'Import csv files into a QLab workspace easily and efficiently.',
  url: 'https://finlayross.me',
  baseUrl: '/csv_to_qlab/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',
  organizationName: 'fross123', // Usually your GitHub org/user name.
  projectName: 'csv_to_qlab', // Usually your repo name.
  trailingSlash: true,

  presets: [
    [
      '@docusaurus/preset-classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          // Please change this to your repo.
          editUrl: 'https://github.com/fross123/csv_to_qlab/edit/main/website/',
        },
        blog: {
          showReadingTime: false,
          // Please change this to your repo.
          editUrl:
            'https://github.com/fross123/csv_to_qlab/edit/main/website/releases/',
          blogTitle: 'CSV to QLab Releases',
          blogDescription: 'CSV to QLab Release Log',
          blogSidebarTitle: "Recent Releases",
          postsPerPage: 'ALL',
          routeBasePath: "releases",
          path: './releases',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
        sitemap: {
          changefreq: 'weekly',
          priority: 0.5,
        },
      }),
    ],
  ],
  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      image: 'img/logo.png',
      gtag: {
        trackingID: 'G-VTFHGK2SN2',
        // Optional fields.
        anonymizeIP: true, // Should IPs be anonymized?
      },
      announcementBar: {
        id: 'support_us',
        content:
          '🌟 If you are enjoying CSV to QLab please give us a star on <a target="_blank" href="https://www.github.com/fross123/csv_to_qlab">Github!</a>!',
        backgroundColor: 'rgba(0, 0, 0, 0.3)',
        textColor: '#091E42',
        isCloseable: false,
      },
      navbar: {
        title: 'CSV to QLab',
        logo: {
          alt: 'csv-to-qlab-Logo',
          src: 'img/csv_to_qlab_logo.svg',
        },
        items: [
          {
            type: 'doc',
            docId: 'intro',
            position: 'left',
            label: 'Tutorial',
          },
          {to: '/releases', label: 'Releases', position: 'left'},
          {
            href: 'https://github.com/fross123/csv_to_qlab',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Docs',
            items: [
              {
                label: 'Tutorial',
                to: '/docs/intro',
              },
            ],
          },
          {
            title: 'More',
            items: [
              {
                label: 'Releases',
                to: '/releases',
              },
              {
                label: 'GitHub',
                href: 'https://github.com/fross123/csv_to_qlab',
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} CSV to QLab, Inc. Built with Docusaurus.`,
      },
      prism: {
        theme: lightCodeTheme,
        darkTheme: darkCodeTheme,
      },
    }),
};

module.exports = config;
