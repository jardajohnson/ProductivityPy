'use strict';

const getData = () => {
	fetch('https://zenquotes.io/api/quotes/')
		.then((response) => response.json())
		.then((data) => console.log(data));
};

getData();