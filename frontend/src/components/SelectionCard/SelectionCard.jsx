import React, { useEffect, useState } from 'react';
import { Box, Container } from '@mui/material';
import SelectAcademicYear from '../SelectAcademicYear/SelectAcademicYear';
import SelectInstitution from '../SelectInstitution/SelectInstitution';
import SelectAgreementInstitution from '../SelectAgreementInstitution/SelectAgreementInstitution';

function SelectionCard({}) {
  return (
    <Container component="main" maxWidth="xs">
      <Box
        sx={{
          marginTop: 8,
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          bgcolor: 'background.paper',
          borderRadius: 1,
          p: 4,
          border: '1px solid',
        }}
      >
        <SelectAcademicYear />
        <SelectInstitution />
        <SelectAgreementInstitution />
      </Box>
    </Container>
  );
}

export default SelectionCard;
