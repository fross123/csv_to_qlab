import React from 'react';
import clsx from 'clsx';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import styles from './index.module.css';
import HomepageFeatures from '../components/HomepageFeatures';
import Logo from '@site/static/img/logo.svg';


function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <Logo title="CSV to QLab Logo" className="logo" height="10em"/>
        <h1 className="hero__title">{siteConfig.title}</h1>
        <p className="hero__subtitle">{siteConfig.tagline}</p>
        <div className={styles.buttons}>
          <Link
            className="button button--secondary button--lg"
            to="/docs/tutorial-basics/installation">
            CSV Import Tutorial
          </Link>
        </div>
        <div className={styles.buttons}>
          <Link
            className="button button--secondary button--lg"
            to="https://github.com/fross123/csv_to_qlab/releases/latest/download/CSV-To-QLab.dmg">
            Skip Ahead and Download Now
          </Link>
        </div>
      </div>
    </header>
  );
}

export default function Home() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`Hello from ${siteConfig.title}`}
      description="Import csv files into a QLab workspace easily and efficiently.">
      <HomepageHeader />
      <main>
        <HomepageFeatures />
      </main>
    </Layout>
  );
}
