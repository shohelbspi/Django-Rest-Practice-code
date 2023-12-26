// src/components/ListPage.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ListPage = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://localhost:8000/student-list/');
        setData(response.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      <h1>List Page</h1>
      <table style={{ borderCollapse: 'collapse', width: '100%' }}>
        <thead>
          <tr style={{ backgroundColor: '#f2f2f2' }}>
            <th style={tableHeaderStyle}>Roll</th>
            <th style={tableHeaderStyle}>Name</th>
            <th style={tableHeaderStyle}>Department</th>
          </tr>
        </thead>
        <tbody>
          {data.map(item => (
            <tr key={item.id} style={{ borderBottom: '1px solid #ddd' }}>
              <td style={tableCellStyle}>{item.roll}</td>
              <td style={tableCellStyle}>{item.name}</td>
              <td style={tableCellStyle}>{item.dep}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

const tableHeaderStyle = {
  padding: '12px',
  textAlign: 'left',
  borderBottom: '1px solid #ddd',
};

const tableCellStyle = {
  padding: '8px',
  textAlign: 'left',
};

export default ListPage;