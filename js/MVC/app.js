(function(){

"use strict";

// ================ Model ======================
const countryList = {
	  selectedItem:null,
		countries: [
			{name: 'Canada' , continent: "North America", flagUrl: 'http://flagpedia.net/data/flags/normal/ca.png', capital: "Ottawa", language: "English and French"},
			{name: 'USA' , continent: "North America", flagUrl: 'http://flagpedia.net/data/flags/normal/us.png', capital: "New York", language: "English"},
			{name: 'Singapore' , continent: "Asia", flagUrl: 'http://flagpedia.net/data/flags/normal/sg.png', capital: "Singapore", language: "English, Tamil, Malay, Mandarin"}
		]
};


// ================ Controller ==================
const countryListApp = {

	init:function(){
		// set first index of an array object as a currentItem
		countryList.selectedItem = countryList.countries[0];



		// initialize two view - ListView (left) and DetailsView (right)
		countryListView.init();
		countryDetailsView.init();

	},

	getCountryList:function(){
		return countryList.countries;
	},

	getSelectedObject:function(){
		return countryList.selectedItem;
	},

	setSelectedObject:function(newSelectedObj){
		countryList.selectedItem = newSelectedObj;
	}

}

// ================ View ======================


// listview
const countryListView = {

		init:function(){
			this.cacheDom();
			this.render();
		},

		cacheDom:function(){
			// cacheDom
			this.$ul = $("#contry-list");
		},

		doClickListItem:function(selectedCountryObject){
			return function(){
				countryListApp.setSelectedObject(selectedCountryObject);
				countryDetailsView.render();
			}
		},

		render:function(){

			// temp vars
			let i, $li, $lichild;

			// add and give event listener at the same time
			const clArray = countryListApp.getCountryList();

			// ----- loop -------
			for(i = 0; i < clArray.length; i++) {
				console.log(clArray[i].name);

				// you could use templet for this
				$li = document.createElement("li");
				$li.innerHTML = `<div class="img-view">
									<img src="${ clArray[i].flagUrl}"  width="50"/>
								</div>

								 <div class="text-view">
							         <h2>${ clArray[i].name}</h2>
							         <h3>${ clArray[i].continent}</h3>
							        </div>
								`;

			  // adding event listener to li
			   $li.addEventListener("click", this.doClickListItem(clArray[i]));

			  // append li to ul
			   this.$ul.append($li);

			}
			// ----- loop -------

		}

}

// detailsview
const countryDetailsView = {
	init:function(){
		this.cacheDOM();
		this.render();
	},

	cacheDOM:function(){
		this.$countryName = $('#country-name');
		this.$countryFlag = $('#country-flag');
		this.$countryCapital = $('#country-capital');
		this.$countryLanguage = $('#country-language');
	},

	render:function(){
		var selectedCountryObj = countryListApp.getSelectedObject();
		this.$countryName.html(selectedCountryObj.name);
		this.$countryFlag.attr("src", selectedCountryObj.flagUrl);
		this.$countryCapital.html(selectedCountryObj.capital);
		this.$countryLanguage.html(selectedCountryObj.language);
	}
}


// ================ Start Point ======================
countryListApp.init();


})();