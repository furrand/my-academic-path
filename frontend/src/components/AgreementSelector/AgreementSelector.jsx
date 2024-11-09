import React, { useEffect, useState } from 'react';
import useFetch from '../../hooks/useFetch';
import { Autocomplete, TextField } from '@mui/material';

function AgreementSelector() {
  const [institutions, setInstitutions] = useState([
    { label: 'Diablo Valley College' },
    { label: 'Berkeley City College' },
  ]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);

  useEffect(() => {
    //const { isLoading, serverError, apiData } = useFetch(
    //  'GET',
    //  'https://127.0.0.1:8000/api',
    //  {},
    //);
    //setInstitutions(null);
    setLoading(false);
    setError(true);
    //setInstitutions(apiData);
    //setLoading(isLoading);
    //setError(serverError);
  }, []);

  return (
    <>
      {loading && <p>Data is being loaded</p>}
      {!loading && (
        <Autocomplete
          disablePortal
          options={institutions}
          renderInput={(params) => (
            <TextField
              {...params}
              label="Institution"
              placeholder="Select an Institution"
            />
          )}
          sx={{ width: 300 }}
        />
      )}
    </>
  );
}

export default AgreementSelector;
