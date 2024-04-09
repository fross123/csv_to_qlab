import React from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
// import styles from './HomepageFeatures.module.css';

const BadgeList = [
    {
        link: 'https://img.shields.io/github/v/release/fross123/csv_to_qlab?style=for-the-badge',
        alt: "version Number"
    },
    // {
    //     link: 'https://img.shields.io/badge/Donate-PayPal?style=for-the-badge&logo=paypal&labelColor=lightgrey&color=blue&link=https%3A%2F%2Fwww.paypal.com%2Fpaypalme%2Ffinlayross',
    //     alt: 'donate-paypal',
    //     button_link: "https://www.paypal.com/paypalme/FinlayRoss"
    // },
    {
        link: 'https://img.shields.io/github/downloads/fross123/csv_to_qlab/total?style=for-the-badge&label=All%20Downloads',
        alt: 'total-downloads'
    },
    {
        link: 'https://img.shields.io/github/downloads/fross123/csv_to_qlab/latest/total?style=for-the-badge',
        alt: 'latest-version-downloads'
    },
    {
        link: "https://img.shields.io/github/release-date/fross123/csv_to_qlab?style=for-the-badge&label=Last%20Release",
        alt: 'last-updated'
    },
    {
        link: 'https://img.shields.io/github/license/fross123/csv_to_qlab?style=for-the-badge',
        alt: 'license'
    },
    {
        link: 'https://img.shields.io/github/actions/workflow/status/fross123/csv_to_qlab/pytest.yml?style=for-the-badge&label=Pytest',
        alt: 'pytest-status'
    },
    
]

const OperatingSystemsList = [
    {
        link: 'https://img.shields.io/badge/Works_On-MacOS_11_or_later-blue?style=for-the-badge&logo=apple',
        alt: 'works on logo',
    },
]


function Badge({link, alt, button_link}) {
    if (button_link) {
        return (
            <Link
                to={button_link}>
                <img src={link} alt={alt} style={{padding: ".5em"}}></img>
            </Link>
        )
    } else {
        return (
            <img src={link} alt={alt} style={{padding: ".5em"}}></img>
        )
    }
}

export default function Badges() {
    return (
        <div className="container" style={{padding: "3em"}}>
            {BadgeList.map((props, idx) => (
                <Badge key={idx} {...props} />
            ))}
            {OperatingSystemsList.map((props, idx) => (
                <Badge key={idx} {...props} />
            ))}
        </div>
    );
}
