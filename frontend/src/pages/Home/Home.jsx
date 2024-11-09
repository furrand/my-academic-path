import React from 'react';
import { Typography, Stack, Container } from '@mui/material';
import Counter from '@/components/Counter/Counter';
import TemplateTester from '@/components/TemplateTester/TemplateTester';
import AgreementSelector from '../../components/AgreementSelector/AgreementSelector';

function Home() {
  return (
    <Container sx={{ py: 2, position: 'relative' }}>
      <Stack gap={1} my={2}>
        <Typography textAlign="center" variant="h2">
          Better Assist
        </Typography>
      </Stack>
      <AgreementSelector />
    </Container>
  );
}

export default Home;
