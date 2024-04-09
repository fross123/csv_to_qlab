// DropdownButton.js

import React, { useState } from 'react';
import Link from '@docusaurus/Link';
import Select from 'react-select';
import styles from './../pages/index.module.css';


const DropdownButton = ({buttonClassName, options }) => {
  const [selectedOption, setSelectedOption] = useState(options[0].value);

  const handleDropdownChange = (e) => {
    setSelectedOption(e.value);
  };

  const getButtonLink = () => {
    const selectedOptionData = options.find((opt) => opt.value === selectedOption);
    return selectedOptionData ? selectedOptionData.link : '#';
  };

  return (
    <div className='download-select-button'>
      <Select 
        theme={(theme) => ({
          ...theme,
          borderRadius: 0,
          colors: {
            ...theme.colors,
            primary25: 'pink',
            primary: 'black',
          },
        })}
        id="dropdown" defaultValue={options[0]}
        onChange={handleDropdownChange}
        options={options}>
        </Select>

      <div className={styles.buttons}>
        <Link
          className={buttonClassName}
          to={getButtonLink()}>
          Download
        </Link>
      </div>
    </div>
  );
};

export default DropdownButton;
