import React, { useEffect, useState } from 'react';
import { Container, Box, InputLabel } from '@mui/material';
import Select from 'react-select';
import { INST_CATEGORY } from '../../utils/constants';
import { useGetInstitutionsQuery } from '../../app/api/apiSlice';

function SelectAgreementInstitution() {
  // TODO: Error handling
  const {
    data = [],
    isLoading,
    isSuccess,
    isError,
    error,
  } = useGetInstitutionsQuery();

  const [groupedInstitutions, setGroupedInstitutions] = useState({
    cccOptions: [],
    csuOptions: [],
    ucOptions: [],
    aiccuOptions: [],
  });

  useEffect(() => {
    if (isSuccess) {
      const cccOptions = [];
      const csuOptions = [];
      const ucOptions = [];
      const aiccuOptions = [];

      data.forEach((item) => {
        item.names?.forEach((elem) => {
          if (elem.hide_in_list === false) {
            const inst = { ...item, label: elem.name };

            switch (item.category) {
              case INST_CATEGORY.CSU:
                csuOptions.push(inst);
                break;
              case INST_CATEGORY.UC:
                ucOptions.push(inst);
                break;
              case INST_CATEGORY.CCC:
                cccOptions.push(inst);
                break;
              case INST_CATEGORY.AICCU:
                aiccuOptions.push(inst);
                break;
              default:
                break;
            }
          }
        });
      });

      const sortFunc = (a, b) => {
        if (a.label < b.label) {
          return -1;
        }
        if (a.label > b.label) {
          return 1;
        }
        return 0;
      };

      cccOptions.sort(sortFunc);
      csuOptions.sort(sortFunc);
      ucOptions.sort(sortFunc);
      aiccuOptions.sort(sortFunc);

      setGroupedInstitutions({
        cccOptions,
        csuOptions,
        ucOptions,
        aiccuOptions,
      });
    }
  }, [isSuccess]);

  const opts = [
    {
      label: 'California Community Colleges (CCC)',
      options: groupedInstitutions.cccOptions,
    },
    {
      label: 'California State University (CSU)',
      options: groupedInstitutions.csuOptions,
    },
    {
      label: 'University of California (UC)',
      options: groupedInstitutions.ucOptions,
    },
    {
      label: 'Independent Universities (AICCU)',
      options: groupedInstitutions.aiccuOptions,
    },
  ];

  return (
    <Box sx={{ marginBottom: '10px', width: '100%' }}>
      <InputLabel shrink htmlFor="Institution" sx={{ marginBottom: 0 }}>
        Agreements with Other Institutions
      </InputLabel>
      {/* <Select options={opts} /> */}
      <Select
        options={opts}
        styles={{
          container: (provided) => ({
            ...provided,
            width: '100%',
          }),
          control: (provided) => ({
            ...provided,
            width: '100%',
          }),
        }}
      />
    </Box>
  );
}

export default SelectAgreementInstitution;
