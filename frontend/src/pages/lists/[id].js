import React from 'react';
import { useRouter } from 'next/router'
import { ThemeProvider } from 'theme-ui';
import theme from 'theme';

import Layout from 'components/layout';
import ListBanner from 'sections/lists-banner';
import ListContent from 'sections/list-content';
import KeyFeature from 'sections/key-feature';

export default function ListPage() {
  // const router = useRouter()
  // const { id } = router.query
  
  return (
    <ThemeProvider theme={theme}>
      <Layout>
        <ListBanner /> 
        <ListContent />
      </Layout>
    </ThemeProvider>
  ); 
}
