import React from 'react';
import clsx from 'clsx';
import styles from './HomepageFeatures.module.css';

const FeatureList = [
  {
    title: 'Easy to Use',
    Svg: require('../../static/img/pink-cake.svg').default,
    description: (
      <>
        CSV to QLab was designed from the ground up to be easily installed and
        used to get your cues imported and running your shows quickly.
      </>
    ),
  },
  {
    title: 'Saves Time',
    Svg: require('../../static/img/alarm-clock.svg').default,
    description: (
      <>
        Often certain cues in QLab require essentially data entry.
        We already create cue sheets, why not use that to create the cues in QLab too?
      </>
    ),
  },
  {
    title: 'Still Growing and Expanding',
    Svg: require('../../static/img/cartoon-rocket.svg').default,
    description: (
      <>
        This is a modern project built to last. We will continue to update
        as suggestions come in. We want to improve your workflow so you can get back to
        running shows as quickly as possible.
      </>
    ),
  },
];

function Feature({Svg, title, description}) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} alt={title} />
      </div>
      <div className="text--center padding-horiz--md">
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
