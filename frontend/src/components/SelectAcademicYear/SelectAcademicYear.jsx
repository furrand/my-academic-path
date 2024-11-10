import React, { useEffect, useState } from 'react';
import { Container, Box, InputLabel } from '@mui/material';
import Select from 'react-select';
import { useGetAcademicYearQuery } from '../../app/api/apiSlice';

function SelectAcademicYear() {
  // TODO: Error handling
  const {
    data = [],
    isLoading,
    isSuccess,
    isError,
    error,
  } = useGetAcademicYearQuery();

  const opts = [];

  useEffect(() => {
    data.forEach((item) => {
      if (item.fall_year < 2025) {
        const next_year = item.fall_year + 1;
        const year_label = item.fall_year + ' - ' + next_year;
        opts.push({
          id: item.id,
          label: year_label,
          fall_year: item.fall_year,
        });
      }
    });
    opts.sort((a, b) => b.fall_year - a.fall_year);
    console.log('YEARS: ', opts);
  }, [isSuccess]);

  return (
    <Box sx={{ marginBottom: '10px', width: '100%' }}>
      <InputLabel shrink htmlFor="Academic Year" sx={{ marginBottom: 0 }}>
        Academic Year
      </InputLabel>
      {/* TODO: Set default value. This should probably be hardcoded before */}
      {/* the data is fetched. Also - figure out why after something is */}
      {/* selected, then every other option also gets selected */}
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

export default SelectAcademicYear;
