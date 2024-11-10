import React from 'react';
import { Typography, Stack, Container } from '@mui/material';
import SelectionCard from '../../components/SelectionCard/SelectionCard';

function Home() {
  return (
    <Container sx={{ py: 2, position: 'relative' }}>
      <Stack gap={1} my={2}>
        <Typography textAlign="center" variant="h2">
          Better Assist
        </Typography>
      </Stack>
      <SelectionCard />
    </Container>
  );
}

export default Home;
