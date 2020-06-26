import React, { FC, useEffect } from 'react';

const DjangoAdminFallback: FC<{}> = ({ route }) => {

  useEffect(() => {
    window.location.href = `${window.location.origin}/admin${route.path}`;
  }, []);

  return <React.Fragment />;
};

export default DjangoAdminFallback;
