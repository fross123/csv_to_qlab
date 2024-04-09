import React from 'react';
import clsx from 'clsx';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import styles from './index.module.css';
import HomepageFeatures from '../components/HomepageFeatures';
import Badges from '../components/StatusBadges.js';
import Logo from '@site/static/img/logo.svg';

import DropdownButton from './../components/DropdownButton.js';


function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  const options = [
    { label: 'macOS 14 (Latest)', value: 'macos14', link: 'https://github.com/fross123/csv_to_qlab/releases/latest/download/CSV-To-QLab.dmg' },
    { label: 'macOS 13', value: 'macos13', link: 'https://github.com/fross123/csv_to_qlab/releases/latest/download/CSV-To-QLab-macos13.dmg' },
    { label: 'macOS 12', value: 'macos12', link: 'https://github.com/fross123/csv_to_qlab/releases/latest/download/CSV-To-QLab-macos12.dmg' },
    { label: 'macOS 11', value: 'macos11', link: 'https://github.com/fross123/csv_to_qlab/releases/latest/download/CSV-To-QLab-macos11.dmg' },
  ];
  const buttonClassName = "button button--secondary button--lg"


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
        <hr></hr>
        <p className='hero__subtitle'>Or... skip ahead and download now!</p>

        <DropdownButton buttonClassName={buttonClassName} options={options} />
        
        <Badges />
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
