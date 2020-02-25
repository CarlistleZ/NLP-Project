cities = ['', 'Aberdeen', 'Abilene', 'Akron', 'Albany', 'Albuquerque', 'Alexandria',
          'Allentown', 'Amarillo', 'Anaheim', 'Anchorage', 'Ann Arbor', 'Antioch',
          'Apple Valley', 'Appleton', 'Arlington', 'Arvada', 'Asheville', 'Athens',
          'Atlanta', 'Atlantic City', 'Augusta', 'Aurora', 'Austin', 'Bakersfield',
          'Baltimore', 'Barnstable', 'Baton Rouge', 'Beaumont', 'Bel Air', 'Bellevue',
          'Berkeley', 'Bethlehem', 'Billings', 'Birmingham', 'Bloomington', 'Boise',
          'Boise City', 'Bonita Springs', 'Boston', 'Boulder', 'Bradenton', 'Bremerton',
          'Bridgeport', 'Brighton', 'Brownsville', 'Bryan', 'Buffalo', 'Burbank',
          'Burlington', 'Cambridge', 'Canton', 'Cape Coral', 'Carrollton', 'Cary',
          'Cathedral City', 'Cedar Rapids', 'Champaign', 'Chandler', 'Charleston',
          'Charlotte', 'Chattanooga', 'Chesapeake', 'Chicago', 'Chula Vista',
          'Cincinnati', 'Clarke County', 'Clarksville', 'Clearwater', 'Cleveland',
          'College Station', 'Colorado Springs', 'Columbia', 'Columbus', 'Concord',
          'Coral Springs', 'Corona', 'Corpus Christi', 'Costa Mesa', 'Dallas', 'Daly City',
          'Danbury', 'Davenport', 'Davidson County', 'Dayton', 'Daytona Beach', 'Deltona',
          'Denton', 'Denver', 'Des Moines', 'Detroit', 'Downey', 'Duluth', 'Durham',
          'El Monte', 'El Paso', 'Elizabeth', 'Elk Grove', 'Elkhart', 'Erie', 'Escondido',
          'Eugene', 'Evansville', 'Fairfield', 'Fargo', 'Fayetteville', 'Fitchburg',
          'Flint', 'Fontana', 'Fort Collins', 'Fort Lauderdale', 'Fort Smith',
          'Fort Walton Beach', 'Fort Wayne', 'Fort Worth', 'Frederick', 'Fremont',
          'Fresno', 'Fullerton', 'Gainesville', 'Garden Grove', 'Garland', 'Gastonia',
          'Gilbert', 'Glendale', 'Grand Prairie', 'Grand Rapids', 'Grayslake', 'Green Bay',
          'GreenBay', 'Greensboro', 'Greenville', 'Gulfport-Biloxi', 'Hagerstown',
          'Hampton', 'Harlingen', 'Harrisburg', 'Hartford', 'Havre de Grace', 'Hayward',
          'Hemet', 'Henderson', 'Hesperia', 'Hialeah', 'Hickory', 'High Point', 'Hollywood',
          'Honolulu', 'Houma', 'Houston', 'Howell', 'Huntington', 'Huntington Beach',
          'Huntsville', 'Independence', 'Indianapolis', 'Inglewood', 'Irvine', 'Irving',
          'Jackson', 'Jacksonville', 'Jefferson', 'Jersey City', 'Johnson City', 'Joliet',
          'Kailua', 'Kalamazoo', 'Kaneohe', 'Kansas City', 'Kennewick', 'Kenosha', 'Killeen',
          'Kissimmee', 'Knoxville', 'Lacey', 'Lafayette', 'Lake Charles', 'Lakeland',
          'Lakewood', 'Lancaster', 'Lansing', 'Laredo', 'Las Cruces', 'Las Vegas',
          'Layton', 'Leominster', 'Lewisville', 'Lexington', 'Lincoln', 'Little Rock',
          'Long Beach', 'Lorain', 'Los Angeles', 'Louisville', 'Lowell', 'Lubbock',
          'Macon', 'Madison', 'Manchester', 'Marina', 'Marysville', 'McAllen', 'McHenry',
          'Medford', 'Melbourne', 'Memphis', 'Merced', 'Mesa', 'Mesquite', 'Miami',
          'Milwaukee', 'Minneapolis', 'Miramar', 'Mission Viejo', 'Mobile', 'Modesto',
          'Monroe', 'Monterey', 'Montgomery', 'Moreno Valley', 'Murfreesboro', 'Murrieta',
          'Muskegon', 'Myrtle Beach', 'Naperville', 'Naples', 'Nashua', 'Nashville',
          'New Bedford', 'New Haven', 'New London', 'New Orleans', 'New York',
          'New York City', 'Newark', 'Newburgh', 'Newport News', 'Norfolk', 'Normal',
          'Norman', 'North Charleston', 'North Las Vegas', 'North Port', 'Norwalk',
          'Norwich', 'Oakland', 'Ocala', 'Oceanside', 'Odessa', 'Ogden', 'Oklahoma City',
          'Olathe', 'Olympia', 'Omaha', 'Ontario', 'Orange', 'Orem', 'Orlando',
          'Overland Park', 'Oxnard', 'Palm Bay', 'Palm Springs', 'Palmdale', 'Panama City',
          'Pasadena', 'Paterson', 'Pembroke Pines', 'Pensacola', 'Peoria', 'Philadelphia',
          'Phoenix', 'Pittsburgh', 'Plano', 'Pomona', 'Pompano Beach', 'Port Arthur',
          'Port Orange', 'Port Saint Lucie', 'Port St. Lucie', 'Portland', 'Portsmouth',
          'Poughkeepsie', 'Providence', 'Provo', 'Pueblo', 'Punta Gorda', 'Racine',
          'Raleigh', 'Rancho Cucamonga', 'Reading', 'Redding', 'Reno', 'Richland',
          'Richmond', 'Richmond County', 'Riverside', 'Roanoke', 'Rochester', 'Rockford',
          'Roseville', 'Round Lake Beach', 'Sacramento', 'Saginaw', 'Saint Louis',
          'Saint Paul', 'Saint Petersburg', 'Salem', 'Salinas', 'Salt Lake City',
          'San Antonio', 'San Bernardino', 'San Buenaventura', 'San Diego', 'San Francisco',
          'San Jose', 'Santa Ana', 'Santa Barbara', 'Santa Clara', 'Santa Clarita',
          'Santa Cruz', 'Santa Maria', 'Santa Rosa', 'Sarasota', 'Savannah', 'Scottsdale',
          'Scranton', 'Seaside', 'Seattle', 'Sebastian', 'Shreveport', 'Simi Valley',
          'Sioux City', 'Sioux Falls', 'South Bend', 'South Lyon', 'Spartanburg', 'Spokane',
          'Springdale', 'Springfield', 'St. Louis', 'St. Paul', 'St. Petersburg', 'Stamford',
          'Sterling Heights', 'Stockton', 'Sunnyvale', 'Syracuse', 'Tacoma', 'Tallahassee',
          'Tampa', 'Temecula', 'Tempe', 'Thornton', 'Thousand Oaks', 'Toledo', 'Topeka',
          'Torrance', 'Trenton', 'Tucson', 'Tulsa', 'Tuscaloosa', 'Tyler', 'Utica', 'Vallejo',
          'Vancouver', 'Vero Beach', 'Victorville', 'Virginia Beach', 'Visalia', 'Waco',
          'Warren', 'Washington', 'Waterbury', 'Waterloo', 'West Covina', 'West Valley City',
          'Westminster', 'Wichita', 'Wilmington', 'Winston', 'Winter Haven', 'Worcester',
          'Yakima', 'Yonkers', 'York', 'Youngstown']

airports = ['Aberdeen Regional Airport', 'Abilene Regional Airport', 'Abraham Lincoln Capital Airport',
            'Adak Airport', 'Adirondack Regional Airport', 'Aguadilla Airport', 'Akron-Canton Airport',
            'Alakanuk Airport', 'Alamogordo-White Sands Regional Airport', 'Albany International Airport',
            'Albuquerque International Sunport', 'Alexandria International Airport', 'Allegheny County Airport',
            'Allen Aaf Airport', 'Alliance Municipal Airport', 'Alpena County Regional Airport',
            'Altoona-Blair County Airport', 'Amarillo International Airport', 'Ambler Airport',
            'Anacortes Airport', 'Anaktuvuk Pass Airport', 'Anchorage International Airport',
            'Anderson Municipal Airport', 'Anderson Regional Airport', 'Angoon Seaplane Base',
            'Aniak Airport', 'Anniston Municipal Airport', 'Arcata Airport', 'Arnold Palmer Regional Airport',
            'Asheville Regional Airport', 'Aspen-Pitkin County Airport', 'Astoria Regional Airport',
            'Athens Ben Epps Airport', 'Atlanta International Airport', 'Atlantic City International Airport',
            'Atlantic City Municipal Airport Bader Field', 'Atqasuk Edward Burnell Sr Memorial Airport',
            'Augusta Regional Airport', 'Augusta State Airport', 'Austin Straubel International Airport',
            'Austin-Bergstrom International Airport', 'Baltimore   Washington International Airport',
            'Bangor International Airport', 'Barnes Municipal Airport', 'Barnstable Municipal Airport',
            'Barter Island LRRS Airport', 'Baton Rouge International Airport', 'Baudette International Airport',
            'Baxter County Regional Airport', 'Bedford Hanscom Field', 'Bellaire Antrim County Airport',
            'Bellingham International Airport', 'Bemidji Regional Airport', 'Bert Mooney Airport',
            'Bethel Airport', 'Billings Logan International Airport', 'Birmingham International Airport',
            'Bishop International Airport', 'Bismarck Municipal Airport', 'Block Island State Airport',
            'Blue Grass Airport', 'Bob Baker Memorial Airport', 'Boeing Field King County International Airport',
            'Boise Airport', 'Boone County Airport', 'Boston Logan International Airport',
            'Bowling Green-Warren County Regional Airport', 'Bozeman Gallatin Field Airport',
            'Bradford Regional Airport', 'Bradley International Airport', 'Brainerd Lakes Regional Airport',
            'Brazoria County Airport', 'Bremerton National Airport', 'Brookings Municipal Airport',
            'Brownsville South Padre Island International Airport', 'Brunswick Golden Isles Airport',
            'Bryce Canyon Airport', 'Buchanan Field Airport', 'Buckland Airport',
            'Buffalo Niagara International Airport', 'Burbank Bob Hope Airport', 'Burke Lakefront Airport',
            'Burlington International Airport', 'Bush Intercontinental Airport', 'Canyonlands Field',
            'Cape Girardeau Regional Airport', 'Cape May County Airport', 'Carl R Keller Field',
            'Cavern City Air Terminal', 'Cecil Field Airport', 'Cedar City Regional Airport',
            'Cedar Rapids Eastern Iowa Airport', 'Central Illinois Regional Airport',
            'Central Nebraska Regional Airport', 'Central Wisconsin Airport', 'Champaign Willard Airport',
            'Chan Gurney Municipal Airport', 'Chandler Field Airport', 'Charles B. Wheeler Downtown Airport',
            'Charleston International Airport', 'Charleston Yeager Airport', 'Charlevoix Municipal Airport',
            'Charlotte County Airport', 'Charlotte Douglas International Airport',
            'Charlottesville-Albemarle Airport', 'Chattanooga Metropolitan Airport',
            'Chautauqua County Jamestown Airport', 'Chefornak Airport', 'Cherry Capital Airport',
            'Chevak Airport', 'Cheyenne Regional Airport', 'Chicago Midway Airport',
            "Chicago O'hare International Airport", 'Chico Municipal Airport', 'Chippewa County International Airport',
            'Chippewa Valley Regional Airport', 'Chisholm-Hibbing Airport',
            'Cincinnati Municipal Airport Lunken Field', 'Cincinnati   Northern Kentucky International Airport',
            'Cleveland Hopkins International Airport', 'Clinton County Airport', 'Clinton Municipal Airport',
            "Coeur D'alene Airport", 'Cold Bay Airport', 'Coles County Memorial Airport', 'Colorado Springs Airport',
            'Columbia Metropolitan Airport', 'Columbia Regional Airport', 'Columbus Metropolitan Airport',
            'Columbus Municipal Airport', 'Cordova Municipal Airport', 'Corpus Christi International Airport',
            'Cortez Municipal Airport', 'Corvallis Municipal Airport', 'Craig Airport',
            'Craven County Regional Airport', 'Culebra Airport', 'Cuyahoga County Airport',
            'Cyril E King Airport', 'Dallas Love Field', 'Dallas Fort Worth International Airport',
            'Danbury Municipal Airport', 'Dane County Regional Airport', 'Danville Regional Airport',
            'Dare County Regional Airport', 'Dayton International Airport', 'Daytona Beach International Airport',
            'Deadhorse Airport', 'Decatur Airport', 'Deer Valley Municipal Airport', 'Del Rio International Airport',
            'Delaware County Airport', 'Delta County Airport', 'Denver International Airport',
            'Des Moines International Airport', 'Detroit City Airport', 'Detroit Metro Airport',
            'Devils Lake Municipal Airport', 'Dickinson - Theodore Roosevelt Regional Airport',
            'Diego Jimenez Torres Airport', 'Dillingham Airport', 'Dodge City Regional Airport',
            'Donaldson Center Airport', 'Dothan Regional Airport', 'Downtown Manhattan Heliport',
            'Drake Field', 'Draughon-Miller Central Texas Regional Airport', 'Du Bois-Jefferson County Airport',
            'Dubuque Regional Airport', 'Duluth International Airport', 'Durango-La Plata County Airport',
            'Dutchess County Airport', 'Eagle County Regional Airport', 'East Texas Regional Airport',
            'Eastern Oregon Regional Airport At Pendleton', 'Easterwood Airport', 'Edward F. Knapp State Airport',
            'Edward G. Pitka Sr Airport', 'Eek Airport', 'El Paso International Airport', 'Elim Airport',
            'Elkhart Municipal Airport', 'Elko Regional Airport', 'Ellington Field',
            'Elmira   Corning Regional Airport', 'Ely Airport', 'Ely Municipal Airport', 'Emmonak Airport',
            'English Bay Airport', 'Eppley Airfield', 'Erie International Airport', 'Ernest A. Love Field Airport',
            'Esler Regional Airport', 'Essex County Airport', 'Eugene Airport', 'Evansville Regional Airport',
            'Fairbanks International Airport', 'Fairmont Municipal Airport', 'Falls International Airport',
            'Fayetteville Regional Grannis Field Airport', 'Fernando Luis Ribas Dominicci Airport', 'Fitiuta Airport',
            'Flagstaff Pulliam Airport', 'Florence Regional Airport', 'Florida Keys Marathon Airport',
            'Floyd Bennett Memorial Airport', 'Forbes Field Airport', 'Fort Collins-Loveland Municipal Airport',
            'Fort Dodge Regional Airport', 'Fort Lauderdale Hollywood International Airport', 'Fort Smith Airport',
            'Fort Walton Beach Airport', 'Fort Wayne International Airport', 'Fort Worth Meacham International Airport',
            'Fort Yukon Airport', 'Four Corners Regional Airport', 'Fresno Air Terminal', 'Friday Harbor Airport',
            'Friedman Memorial Airport', 'Gainesville Regional Airport', 'Galbraith Lake Airport',
            'Gallup Municipal Airport', 'Galveston Scholes International Airport', 'Gambell Airport',
            'Garden City Regional Airport', 'Gary Regional Airport', 'Gaylord Regional Airport',
            'General Mitchell International Airport', 'Gerald R. Ford International Airport',
            'Gillette-Campbell County Airport', 'Glacier Park International Airport', 'Gogebic-Iron County Airport',
            'Golden Triangle Regional Airport', 'Golovin Airport', 'Goodland Municipal Airport',
            'Grand Canyon National Park Airport', 'Grand Canyon West Airport', 'Grand Forks International Airport',
            'Grand Rapids Itasca County Airport', 'Grant County Airport', 'Grant County International Airport',
            'Great Bend Municipal Airport', 'Great Falls International Airport', 'Greater Binghamton Airport',
            'Greater Rochester International Airport', 'Greater Rockford Airport',
            'Greenbrier Valley Airport', 'Greenville   Spartanburg Airport', 'Griffiss Airpark',
            'Groton-New London Airport', 'Guam International Airport', 'Gulfport-Biloxi International Airport',
            'Gulkana Airport', 'Gunnison-Crested Butte Regional Airport', 'Gustavus Airport',
            'Hagerstown Regional Airport', 'Haines Airport', 'Hana Airport', 'Hancock County-Bar Harbor Airport',
            'Harrisburg International Airport', 'Harrison Marion Regional Airport', 'Hartford-Brainard Airport',
            'Hattiesburg-Laurel Regional Airport', 'Hawkins Field Airport', 'Hays Regional Airport',
            'Hector International Airport', 'Helena Regional Airport', 'Henderson Executive Airport',
            'Henderson Field Airport', 'Henry E Rohlsen Airport', 'Hickory Regional Airport',
            'Hilo International Airport', 'Hilton Head Airport', 'Hobby Airport', 'Hollis Seaplane Base',
            'Homer Airport', 'Honolulu International Airport', 'Hoonah Airport', 'Hooper Bay Airport',
            'Houghton County Memorial Airport', 'Huntsville International Airport', 'Huron Regional Airport',
            'Huslia Airport', 'Huslia Airport', 'Hutchinson Municipal Airport', 'Idaho Falls Regional Airport',
            'Igor I Sikorsky Memorial Airport', 'Iliamna Airport', 'Imperial County Airport',
            'Indianapolis International Airport', 'Inyokern Airport', 'Iron Mountain Airport',
            'Ithaca Tompkins Regional Airport', 'Jack Mc Namara Field Airport', 'Jackson County Airport',
            'Jackson Hole Airport', 'Jackson-Evers International Airport', 'Jacksonville International Airport',
            'Jacksonville Albert J Ellis Airport', 'Jamestown Regional Airport', 'Jefferson City Memorial Airport',
            'John F. Kennedy International Airport', 'John Wayne Airport', 'Johnstown-Cambria County Airport',
            'Jonesboro Municipal Airport', 'Joplin Regional Airport', 'Juneau International Airport',
            'Kahului Airport', 'Kake Airport', 'Kalamazoo Battle Creek International Airport',
            'Kalskag Airport', 'Kaltag Airport', 'Kansas City International Airport',
            'Karl Stefan Memorial Airport', 'Kasigluk Airport', 'Kearney Municipal Airport',
            'Keene Dillant-Hopkins Airport', 'Kenai Municipal Airport', 'Kenosha Regional Airport',
            'Ketchikan International Airport', 'Key Field Airport', 'Key West International Airport',
            'Killeen-Fort Hood Regional Airport', 'King Cove Airport', 'King Salmon Airport',
            'Kingman Airport', 'Kinston Regional Jetport', 'Kipnuk Airport', 'Kirksville Regional Airport',
            'Kivalina Airport', 'Klamath Falls Airport', 'Klawock Airport', 'Knox County Regional Airport',
            'Kodiak Airport', 'Kodiak Municipal Airport', 'Kona International Airport', 'Kongiganak Airport',
            'Kotlik Airport', 'Koyuk Airport', 'Kwethluk Airport', 'Kwigillingok Airport', 'Kwigillingok Airport',
            'La Crosse Municipal Airport', 'La Guardia Airport', 'Lafayette Regional Airport',
            'Lake Charles Regional Airport', 'Lake Havasu City Airport', 'Lake Hood Airport', 'Lake Tahoe Airport',
            'Lakefront Airport', 'Lakeland Linder Regional Airport', 'Lamar Municipal Airport',
            'Lambert-St. Louis International Airport', 'Lanai Airport', 'Lancaster Airport',
            'Lansing Capital City Airport', 'Laramie Regional Airport', 'Laredo International Airport',
            'Larsen Bay Airport', 'Las Cruces International Airport', 'Laughlin Bullhead International Airport',
            'Lawton-Fort Sill Regional Airport', 'Lea County Regional Airport', 'Lebanon Municipal Airport',
            'Lee C Fine Memorial Airport', 'Lehigh Valley International Airport', 'Lewiston-Nez Perce County Airport',
            'Liberal Municipal Airport', 'Lihue Airport', 'Lincoln Airport', 'Little Rock National Airport',
            'Long Beach Airport', 'Lorain County Regional Airport', 'Los Angeles International Airport',
            'Louisville International Airport', 'Lubbock International Airport',
            'Luis Munoz Marin International Airport', 'Lynchburg Regional Airport Preston Glenn Field',
            'M Graham Clark - Taney County Airport', 'Macarthur Airport', 'Magic Valley Regional Airport',
            'Mammoth Yosemite Airport', 'Manchester Airport', 'Manhattan Regional Airport', 'Manistee County-Blacker',
            'Mankato Regional Airport', 'Manokotak Airport', 'Mansfield Lahm Regional Airport', 'Marshall Airport',
            'Marshall Don Hunter Sr', 'Marshall Don Hunter Sr Airport', "Martha's Vineyard Airport",
            'Mason City Municipal Airport', 'Massena International Airport', 'Mayaquez Airport', 'Mc Clellan Airfield',
            'Mc Clellan-Palomar Airport', 'Mc Cook Regional Airport', 'Mc Kellar-Sipes Regional Airport',
            'Mc Minnville Municipal Airport', 'Mcallen-Miller International Airport', 'Mccarran International Airport',
            'McGrath Airport', 'Mcghee Tyson Airport', 'Meadows Field Airport',
            'Medford Rogue Valley International Airport', 'Melbourne International Airport', 'Memorial Field Airport',
            'Memphis Airport', 'Menominee-Marinette Twin County Airport', 'Merced Municipal Airport',
            'Mercedita Airport', 'Merrill C Meigs Field', 'Merrill Field', 'Metlakatla Airport', 'Miami Airport',
            'Miami International Airport', 'Mid Delta Regional Airport', 'Mid-Ohio Valley Regional Airport',
            'Midamerica Airport', 'Middle Bass Island Airport', 'Middle Georgia Regional Airport',
            'Midland International Airport', 'Millington Regional Jetport', 'Millville Municipal Airport',
            'Minneapolis St. Paul International Airport', 'Minot International Airport',
            'Missoula International Airport', 'Mitchell Municipal Airport', 'Mobile Regional Airport',
            'Modesto City-County Airport', 'Molokai Airport', 'Monmouth Executive Airport', 'Monroe County Airport',
            'Monroe Regional Airport', 'Monterey Peninsula Airport', 'Montgomery Regional Airport',
            'Montrose Regional Airport', 'Moore County Airport', 'Morgantown Municipal Airport',
            'Morristown Municipal Airport', 'Morrisville-Stowe State Airport', 'Mount Comfort Airport',
            'Mount Vernon Airport', 'Mountain Village Airport', 'Muskegon County Airport', 'Myrtle Beach Airport',
            'Nantucket Memorial Airport', 'Napakiak Airport', 'Naples Municipal Airport',
            'Nashville International Airport', 'Natrona County International Airport',
            'New Bedford Regional Airport', 'New Castle Airport', 'New Orleans International Airport',
            'Newark Liberty International Airport', 'Newport Municipal Airport',
            'Newport News Williamsburg International Airport', 'Newport State Airport', 'Newport State Airport',
            'Newtok Airport', 'Noatak Airport', 'Nome Airport', 'Norfolk International Airport',
            'North Bend Municipal Airport', 'North Central State Airport', 'North Las Vegas Air Terminal',
            'North Platte Regional Airport Lee Bird Field', 'Northern Maine Regional Airport',
            'Northwest Alabama Regional Airport', 'Northwest Arkansas Regional Airport', 'Nuiqsut Airport',
            'Nulato Airport', 'Nunapitchuk Airport', 'Oakland County International Airport',
            'Oakland International Airport', 'Ocala International Airport', 'Ofu Airport', 'Ogden-Hinckley Airport',
            'Ogdensburg International Airport', 'Ohio State University Airport',
            'Olathe New Century Aircenter Airport', 'Old Harbor Airport', 'Olympia Airport', 'Oneida County Airport',
            'Ontario International Airport', 'Orcas Island Airport', 'Orlando International Airport',
            'Orlando Sanford International Airport', 'Ottumwa Industrial Airport', 'Outagamie County Regional Airport',
            'Owensboro-Daviess County Airport', 'Oxnard Airport', 'Paducah Barkley Regional Airport',
            'Page Municipal Airport', 'Pago Pago International Airport', 'Palm Beach International Airport',
            'Palm Springs International Airport', 'Palmdale Regional Airport',
            'Panama City-Bay County International Airport', 'Pangborn Memorial Airport',
            'Paso Robles Municipal Airport', 'Pease International Airport', 'Pellston Regional Airport',
            'Pensacola Regional Airport', 'Peoria Regional Airport', 'Petersburg Airport',
            'Philadelphia International Airport', 'Phoenix Goodyear Airport',
            'Phoenix Sky Harbor International Airport', 'Piedmont Triad International Airport',
            'Pierre Regional Airport', 'Pilot Station Airport', 'Pinal Airpark', 'Pitt-Greenville Airport',
            'Pittsburgh International Airport', 'Pocatello Regional Airport', 'Point Hope Airport',
            'Ponca City Regional Airport', 'Port Columbus International Airport', 'Port Graham Airport',
            'Port Heiden Airport', 'Port Lions Airport', 'Porter County Municipal Airport',
            'Portland International Airport', 'Portland International Jetport', 'Prospect Creek Airport',
            'Provincetown Municipal Airport', 'Provo Municipal Airport', 'Pueblo Memorial Airport',
            'Pullman   Moscow Regional Airport', 'Purdue University Airport', 'Put - in - Bay Airport',
            'Quad City International Airport', 'Quincy Regional Airport - Baldwin Field', 'Quinhagak Airport',
            'Quonset State Airport', 'Raleigh County Memorial Airport', 'Raleigh-Durham International Airport',
            'Ralph M Calhoun Memorial Airport', 'Ralph Wien Memorial Airport', 'Rapid City Regional Airport',
            'Reading Regional Airport', 'Redding Municipal Airport', 'Reno-Tahoe International Airport',
            'Republic Airport', 'Rhinelander-Oneida County Airport', 'Richard B Russell Airport',
            'Richmond International Airport', 'Rickenbacker International Airport', 'Riverton Regional Airport',
            'Roanoke Regional Airport', 'Robert (Bob) Curtis Memorial Airport', 'Robert (Bob) Curtis Memorial Airport',
            'Robert J. Miller Air Park', 'Roberts Field', 'Rochester International Airport',
            'Rock Springs-Sweetwater County Airport', 'Rocky Mount-Wilson Regional Airport',
            'Ronald Reagan Washington National Airport', 'Rosecrans Memorial Airport',
            'Roswell Industrial Air Center Airport', 'Rota International Airport', 'Russian Mission Airport',
            'Rutland State Airport', 'Sacramento International Airport', 'Saginaw International Airport',
            'Saint Paul Island Airport', 'Saipan International Airport', 'Salem Municipal Airport - McNary Field',
            'Salina Municipal Airport', 'Salisbury-Ocean City Wicomico Regional Airport',
            'Salt Lake City International Airport', 'San Angelo Regional Airport Mathis Field',
            'San Antonio International Airport', 'San Bernardino International Airport',
            'San Diego International Airport', 'San Francisco International Airport', 'San Jose International Airport',
            'San Luis County Regional Airport', 'San Luis Valley Regional Airport', 'Sand Point Airport',
            'Santa Barbara Airport', 'Santa Fe Municipal Airport', 'Santa Maria Public Airport',
            'Sarasota-Bradenton International Airport', 'Savannah Hilton Head International Airport',
            'Savoonga Airport', 'Sawyer International Airport', 'Scammon Bay Airport',
            'Seattle Tacoma International Airport', 'Selawik Airport', 'Seldovia Airport',
            'Shenandoah Valley Regional Airport', 'Sheridan County Airport', 'Shishmaref Airport',
            'Show Low Regional Airport', 'Shreveport Regional Airport', 'Shungnak Airport',
            'Sidney-Richland Municipal Airport', 'Sierra Blanca Regional Airport', 'Sierra Vista Municipal Airport',
            'Sioux Falls Regional Airport', 'Sioux Gateway Airport', 'Sitka Rocky Gutierrez Airport',
            'Skagway Airport', 'Skylark Field', 'Sloulin Field International Airport', 'Smith Reynolds Airport',
            'Smyrna Airport', 'Snohomish County Airport (Paine Field)', 'Sonoma County Airport',
            'South Bend Regional Airport', 'Southeast Iowa Regional Airport', 'Southeast Texas Regional Airport',
            'Southern California Logistics Airport', 'Southern Illinois Airport',
            'Southern Wisconsin Regional Airport', 'Southwest Florida International Airport',
            'Southwest Georgia Regional Airport', 'Southwest Michigan Regional Airport',
            'Space Coast Regional Airport', 'Spirit Of St Louis Airport', 'Spokane International Airport',
            'Springfield Branson Regional Airport', 'Springfield-Beckley Municipal Airport', 'St Augustine Airport',
            'St Cloud Regional Airport', 'St George Municipal Airport', 'St Louis Regional Airport',
            "St Mary's Airport", 'St Paul Downtown Airport   Holman Field',
            'St. Petersburg-Clearwater International Airport', 'Stebbins Airport', 'Stewart International Airport',
            'Stillwater Regional Airport', 'Stockton Metropolitan Airport', 'Sullivan County International Airport',
            'Sussex County Airport', 'Syracuse Hancock International Airport', 'T.F. Green Airport',
            'Tallahassee Regional Airport', 'Talladega Municipal Airport', 'Tampa International Airport',
            'Taos Regional Airport', 'Telluride Regional Airport', 'Terre Haute International Airport',
            'Teterboro Airport', 'Texarkana Regional Airport', 'Thief River Falls Regional Airport',
            'Thorne Bay Airport', 'Tinian International Airport', 'Togiak Airport', 'Toksook Bay Airport',
            'Toledo Express Airport', 'Trent Lott International Airport', 'Trenton Mercer Airport',
            'Tri-Cities Airport', 'Tri-Cities Regional Airport', 'Tri-State Airport', 'Trident Basin Seaplane Base',
            'Tucson International Airport', 'Tulsa International Airport', 'Tuluksak Airport',
            'Tuntutuliak Airport', 'Tupelo Regional Airport', 'Tuscaloosa Regional Airport',
            'Tweed New Haven Regional Airport', 'Tyler Pounds Regional Airport', 'Unalakleet Airport',
            'Unalaska Airport', 'University Park Airport', 'University-Oxford Airport', 'Valdez Pioneer Field',
            'Valdosta Regional Airport', 'Valley International Airport', 'Venango Regional Airport',
            'Vermilion County Airport', 'Vero Beach Municipal Airport', 'Vicksburg Tallulah Regional Airport',
            'Victoria Regional Airport', 'Vieques Airport', 'Visalia Municipal Airport', 'W K Kellogg Airport',
            'Waco Regional Airport', 'Waimea - Kohala Airport', 'Wainwright Airport', 'Walker Field Airport',
            'Walla Walla Regional Airport', 'Washington Dulles International Airport', 'Waterbury-Oxford Airport',
            'Waterloo Regional Airport', 'Watertown International Airport', 'Watertown Municipal Airport',
            'Waynesville Regional Airport At Forney Field', 'West Yellowstone Airport', 'Westchester County Airport',
            'Westerly State Airport', 'Western Nebraska Regional Airport', 'Westover Metropolitan Airport',
            'Whiteside County Airport', 'Wichita Falls Municipal Airport', 'Wichita Mid-Continent Airport',
            'Wiley Post-Will Rogers Memorial Airport', 'Wilkes-Barre Scranton International Airport',
            'Will Rogers World Airport', 'William H. Morse State Airport', 'William R Fairchild International Airport',
            'Williams Gateway Airport', 'Williamson County Regional Airport', 'Williamsport Regional Airport',
            'Willmar Municipal Airport', 'Wilmington International Airport', 'Wittman Regional Airport',
            'Wokal Field Glasgow International Airport', 'Woodring Municipal Airport', 'Worcester Regional Airport',
            'Worland Municipal Airport', 'Worthington Municipal Airport', 'Wrangell Airport',
            'Yakima Air Terminal Mcallister Field', 'Yakutat Airport', 'Yampa Valley Regional Airport',
            'Yellowstone Regional Airport', 'Youngstown Regional Airport', 'Yuma International Airport']

airlines = [
    'Alaska Airlines', 'AS', 'ASA',
    'Allegiant Air', 'G4', 'AAY'
    'American Airlines', 'AA', 'AAL',
    'Delta Air Lines', 'DL', 'DAL',
    'Frontier Airlines', 'F9', 'FFT',
    'Hawaiian Airlines', 'HA', 'HAL',
    'JetBlue Airways', 'B6', 'JBU',
    'Southwest Airlines', 'WN', 'SWA',
    'Spirit Airlines', 'NK', 'NKS',
    'Sun Country Airlines', 'SY', 'SCX',
    'United Airlines', 'UA', 'UAL',
    'Air Wisconsin', 'ZW', 'AWI',
    'Cape Air', '9K', 'KAP',
    'Commut Air', 'C5', 'UCA',
    'Compass Airlines', 'CP', 'CPZ',
    'Contour Airlines', 'LF', 'VTE',
    'Elite Airways', '7Q', 'MNU',
    'Endeavor Air', '9E', 'EDV',
    'Envoy Air', 'MQ', 'ENY',
    'ExpressJet',
    'GoJet Airlines',
    'Horizon Air',
    'Mesa Airlines',
    'PenAir',
    'Piedmont Airlines',
    'PSA Airlines',
    'Republic Airways',
    'Silver Airways',
    'SkyWest Airlines',
    'Trans States Airlines'
]


airport_codes_txt = '''
Aberdeen, SD (ABR) 
Abilene, TX (ABI)
Adak Island, AK (ADK)
Akiachak, AK (KKI)
Akiak, AK (AKI)
Akron/Canton, OH (CAK)
Akuton, AK (KQA)
Alakanuk, AK (AUK)
Alamogordo, NM (ALM)
Alamosa, CO (ALS)
Albany, NY (ALB)
Albany, OR - Bus service (CVO)
Albany, OR - Bus service (QWY)
Albuquerque, NM (ABQ)
Aleknagik, AK (WKK)
Alexandria, LA (AEX)
Allakaket, AK (AET)
Allentown, PA (ABE)
Alliance, NE (AIA)
Alpena, MI (APN)
Altoona, PA (AOO)
Amarillo, TX (AMA)
Ambler, AK (ABL)
Anaktueuk, AK (AKP)
Anchorage, AK (ANC)
Angoon, AK (AGN)
Aniak, AK (ANI)
Anvik, AK (ANV)
Appleton, WI (ATW)
Arcata, CA (ACV)
Arctic Village, AK (ARC)
Asheville, NC (AVL)
Ashland, KY/Huntington, WV (HTS)
Aspen, CO (ASE)
Athens, GA (AHN)
Atka, AK (AKB)
Atlanta, GA (ATL)
Atlantic City, NJ (AIY)
Atqasuk, AK (ATK)
Augusta, GA (AGS)
Augusta, ME (AUG)
Austin, TX (AUS)
Bakersfield, CA (BFL)
Baltimore, MD (BWI)
Bangor, ME (BGR)
Bar Harbour, ME (BHB)
Barrow, AK (BRW)
Barter Island, AK (BTI)
Baton Rouge, LA (BTR)
Bay City, MI (MBS)
Beaumont/Port Arthur, TX (BPT)
Beaver Creek, CO - Van service (ZBV)
Beaver, AK (WBQ)
Beckley, WV (BKW)
Bedford, MA (BED)
Belleville, IL (BLV)
Bellingham, WA (BLI)
Bemidji, MN (BJI)
Benton Harbor, MI (BEH)
Bethel, AK (BET)
Bethlehem, PA (ABE)
Bettles, AK (BTT)
Billings, MT (BIL)
Biloxi/Gulfport, MS (GPT)
Binghamton, NY (BGM)
Birch Creek, AK (KBC)
Birmingham, AL (BHM)
Bismarck, ND (BIS)
Block Island, RI (BID)
Bloomington, IL (BMI)
Bluefield, WV (BLF)
Boise, ID (BOI)
Boston, MA (BOS)
Boulder, CO - Bus service (XHH)
Boulder, CO - Hiltons Har H (WHH)
Boulder, CO - Municipal Airport (WBU)
Boundary, AK (BYA)
Bowling Green, KY (BWG)
Bozeman, MT (BZN)
Bradford, PA (BFD)
Brainerd, MN (BRD)
Brawnwood, TX (BWD)
Breckonridge, CO - Van service (QKB)
Bristol, VA (TRI)
Brookings, SD (BKX)
Brooks Lodge, AK (RBH)
Brownsville, TX (BRO)
Brunswick, GA (BQK)
Buckland, AK (BKC)
Buffalo, NY (BUF)
Bullhead City/Laughlin, AZ (IFP)
Burbank, CA (BUR)
Burlington, IA (BRL)
Burlington, VT (BTV)
Butte, MT (BTM)
Canton/Akron, OH (CAK)
Cape Girardeau, MO (CGI)
Cape Lisburne, AK (LUR)
Cape Newenham, AK (EHM)
Carbondale, IL (MDH)
Carlsbad, CA (CLD)
Carlsbad, NM (CNM)
Carmel, CA (MRY)
Casper, WY (CPR)
Cedar City, UT (CDC)
Cedar Rapids, IA (CID)
Central, AK (CEM)
Chadron, NE (CDR)
Chalkyitsik, AK (CIK)
Champaign/Urbana, IL (CMI)
Charleston, SC (CHS)
Charleston, WV (CRW)
Charlotte, NC (CLT)
Charlottesville, VA (CHO)
Chattanooga, TN (CHA)
Chefornak, AK (CYF)
Chevak, AK (VAK)
Cheyenne, WY (CYS)
Chicago, IL - Meigs (CGX)
Chicago, IL - All airports (CHI)
Chicago, IL - Midway (MDW)
Chicago, IL - O'Hare (ORD)
Chicken, AK (CKX)
Chico, CA (CIC)
Chignik, AK - Fisheries (KCG)
Chignik, AK - (KCQ)
Chignik, AK - Lagoon (KCL)
Chisana, AK (CZN)
Chisholm/Hibbing, MN (HIB)
Chuathbaluk, AK (CHU)
Cincinnati, OH (CVG)
Circle Hot Springs, AK (CHP)
Circle, AK (IRC)
Clarks Point, AK (CLP)
Clarksburg, WV (CKB)
Clearwater/St Petersburg, FL (PIE)
Cleveland, OH (CLE)
Clovis, NM (CVN)
Cody/Yellowstone, WY (COD)
Coffee Point, AK (CFA)
Coffman Cove, AK (KCC)
Cold Bay, AK (CDB)
College Station, TX (CLL)
Colorado Springs, CO (COS)
Columbia, MO (COU)
Columbia, SC (CAE)
Columbus, GA (CSG)
Columbus, MS (GTR)
Columbus, OH (CMH)
Concord, CA (CCR)
Concordia, KS (CNK)
Copper Mountain, CO - Van service (QCE)
Cordova, AK (CDV)
Corpus Christi, TX (CRP)
Cortez, CO (CEZ)
Craig, AK (CGA)
Crescent City, CA (CEC)
Crooked Creek, AK (CKO)
Cube Cove, AK (CUW)
Cumberland, MD (CBE)

return to top
D
Dallas/Fort Worth, TX (DFW)
Dayton, OH (DAY)
Daytona Beach, FL (DAB)
Decatur, IL (DEC)
Deering, AK (DRG)
Delta Junction, AK (DJN)
Denver, CO - International (DEN)
Denver, CO - Longmont Bus service (QWM)
Des Moines, IA (DSM)
Detroit, MI - All airports (DTT)
Detroit, MI - Metro/Wayne County (DTW)
Devil's Lake, ND (DVL)
Dickinson, ND (DIK)
Dillingham, AK (DLG)
Dodge City, KS (DDC)
Dothan, AL (DHN)
Dubois, PA (DUJ)
Dubuque, IA (DBQ)
Duluth, MN (DLH)
Durango, CO (DRO)
Durham, NC (RDU)
Durham/Raleigh, NC (RDU)
Dutch Harbor, AK (DUT)
Easton, PA (ABE)
Eau Claire, WI (EAU)
Edna Bay, AK (EDA)
Eek, AK (EEK)
Ekuk, AK (KKU)
Ekwok, AK (KEK)
El Centro, CA (IPL)
El Dorado, AR (ELD)
El Paso, TX (ELP)
Elfin Cove, AK (ELV)
Elim, AK (ELI)
Elko, NV (EKO)
Elmira, NY (ELM)
Ely, MN (LYU)
Emmonak, AK (EMK)
Endicott, NY (BGM)
Enid, OK (WDG)
Erie, PA (ERI)
Escanaba, MI (ESC)
Eugene, OR (EUG)
Eureka/Arcata, CA (ACV)
Eureka, NV (EUE)
Evansville, IN (EVV)
Fairbanks, AK (FAI)
Fargo, ND (FAR)
Fayetteville, AR - Municipal/Drake (FYV)
Fayetteville, AR - Northwest Arkansas Regional (XNA)
Fayetteville, NC (FAY)
Flagstaff, AZ (FLG)
Flint, MI (FNT)
Florence, SC (FLO)
Florence/Muscle Shoals/Sheffield, AL (MSL)
Fort Collins/Loveland, CO - Municipal Airport (FNL)
Fort Collins/Loveland, CO - Bus service (QWF)
Fort Dodge, IA (FOD)
Fort Lauderdale, FL (FLL)
Fort Leonard Wood, MO (TBN)
Fort Myers, FL (RSW)
Fort Smith, AR (FSM)
Fort Walton Beach, FL (VPS)
Fort Wayne, IN (FWA)
Fort Worth/Dallas, TX (DFW)
Franklin, PA (FKL)
Fresno, CA (FAT)
Gainesville, FL (GNV)
Gallup, NM (GUP)
Garden City, KS (GCK)
Gary, IN (GYY)
Gillette, WY (GCC)
Gladewater/Kilgore, TX (GGG)
Glasgow, MT (GGW)
Glendive, MT (GDV)
Golovin, AK (GLV)
Goodnews Bay, AK (GNU)
Grand Canyon, AZ - Heliport (JGC)
Grand Canyon, AZ - National Park (GCN)
Grand Forks, ND (GFK)
Grand Island, NE (GRI)
Grand Junction, CO (GJT)
Grand Rapids, MI (GRR)
Grand Rapids, MN (GPZ)
Grayling, AK (KGX)
Great Falls, MT (GTF)
Green Bay, WI (GRB)
Greensboro, NC (GSO)
Greenville, MS (GLH)
Greenville, NC (PGV)
Greenville/Spartanburg, SC (GSP)
Groton/New London, CT (GON)
Gulfport, MS (GPT)
Gunnison, CO (GUC)
Gustavus, AK (GST)
Hagerstown, MD (HGR)
Hailey, ID (SUN)
Haines, AK (HNS)
Hampton, VA (PHF)
Hana, HI - Island of Maui (HNM)
Hanapepe, HI (PAK)
Hancock, MI (CMX)
Hanover, NH (LEB)
Harlingen, TX (HRL)
Harrisburg, PA (MDT)
Harrison, AR (HRO)
Hartford, CT (BDL)
Havasupai, AZ (HAE)
Havre, MT (HVR)
Hayden, CO (HDN)
Hays, KS (HYS)
Healy Lake, AK (HKB)
Helena, MT (HLN)
Hendersonville, NC (AVL)
Hibbing/Chisholm, MN (HIB)
Hickory, NC (HKY)
High Point, NC (GSO)
Hilo, HI - Island of Hawaii (ITO)
Hilton Head, SC (HHH)
Hobbs, NM (HBB)
Hollis, AK (HYL)
Holy Cross, AK (HCR)
Homer, AK (HOM)
Honolulu, HI - Island of Oahu (HNL)
Hoolehua, HI - Island of Molokai (MKK)
Hoonah, AK (HNH)
Hooper Bay, AK (HPB)
Hot Springs, AR (HOT)
Houston, TX - All airports (HOU)
Houston, TX - Hobby (HOU)
Houston, TX - Intercontinental (IAH)
Hughes, AK (HUS)
Huntington, WV/Ashland, KY (HTS)
Huntsville, AL (HSV)
Huron, SD (HON)
Huslia, AK (HSL)
Hyannis, MA (HYA)
Hydaburg, AK (HYG)
Idaho Falls, ID (IDA)
Igiugig, AK (IGG)
Iliamna, AK (ILI)
Imperial, CA (IPL)
Indianapolis, IN (IND)
International Falls, MN (INL)
Inyokern, CA (IYK)
Iron Mountain, MI (IMT)
Ironwood, MI (IWD)
Islip, NY (ISP)
Ithaca, NY (ITH)
Jackson Hole, WY (JAC)
Jackson, MS (JAN)
Jackson, TN (MKL)
Jacksonville, FL (JAX)
Jacksonville, NC (OAJ)
Jamestown, ND (JMS)
Jamestown, NY (JHW)
Janesville, WI (JVL)
Johnson City, NY (BGM)
Johnson City, TN (TRI)
Johnstown, PA (JST)
Jonesboro, AR (JBR)
Joplin, MO (JLN)
Juneau, AK (JNU)
Kahului, HI - Island of Maui, (OGG)
Kake, AK (KAE)
Kakhonak, AK (KNK)
Kalamazoo, MI (AZO)
Kalaupapa, HI - Island of Molokai, (LUP)
Kalskag, AK (KLG)
Kaltag, AK (KAL)
Kamuela, HI - Island of Hawaii, (MUE)
Kansas City, MO (MCI)
Kapalua, HI - Island of Maui, (JHM)
Kasaan, AK (KXA)
Kasigluk, AK (KUK)
Kauai Island/Lihue, HI (LIH)
Kearney, NE (EAR)
Keene, NH (EEN)
Kenai, AK (ENA)
Ketchikan, AK (KTN)
Key West, FL (EYW)
Keystone, CO - Van service (QKS)
Kiana, AK (IAN)
Kilgore/Gladewater, TX (GGG)
Killeen, TX (ILE)
King Cove, AK (KVC)
King Salmon, AK (AKN)
Kingman, AZ (IGM)
Kingsport, TN (TRI)
Kipnuk, AK (KPN)
Kirksville, MO (IRK)
Kivalina, AK (KVL)
Klamath Falls, OR (LMT)
Klawock, AK (KLW)
Knoxville, TN (TYS)
Kobuk, AK (OBU)
Kodiak, AK (ADQ)
Kona, HI - Island of Hawaii (KOA)
Kongiganak, AK (KKH)
Kotlik, AK (KOT)
Kotzebue, AK (OTZ)
Koyukuk, AK (KYU)
Kwethluk, AK (KWT)
Kwigillingok, AK (KWK)
La Crosse, WI (LSE)
Lafayette, IN (LAF)
Lafayette, LA (LFT)
Lake Charles, LA (LCH)
Lake Havasu City, AZ (HII)
Lake Minchumina, AK (LMA)
Lanai City, HI - Island of Lanai (LNY)
Lancaster, PA (LNS)
Lansing, MI (LAN)
Laramie, WY (LAR)
Laredo, TX (LRD)
Las Vegas, NV (LAS)
Latrobe, PA (LBE)
Laurel, MS (PIB)
Lawton, OK (LAW)
Lebanon, NH (LEB)
Levelock, AK (KLL)
Lewisburg, WV (LWB)
Lewiston, ID (LWS)
Lewistown, MT (LWT)
Lexington, KY (LEX)
Liberal, KS (LBL)
Lihue, HI - Island of Kaui (LIH)
Lincoln, NE (LNK)
Little Rock, AR (LIT)
Long Beach, CA (LGB)
Longview, TX (GGG)
Lopez Island, WA (LPS)
Los Angeles, CA (LAX)
Louisville, KY (SDF)
Loveland/Fort Collins, CO - Municipal Airport (FNL) 
Loveland/Fort Collins, CO - Bus service (QWF)
Lubbock, TX (LBB)
Macon, GA (MCN)
Madison, WI (MSN)
Madras, OR (MDJ)
Manchester, NH (MHT)
Manhattan, KS (MHK)
Manistee, MI (MBL)
Mankato, MN (MKT)
Manley Hot Springs, AK (MLY)
Manokotak, AK (KMO)
Marietta, OH/Parkersburg, WV (PKB)
Marion, IL (MWA)
Marquette, MI (MQT)
Marshall, AK (MLL)
Martha's Vineyard, MA (MVY)
Martinsburg, PA (AOO)
Mason City, IA (MCW)
Massena, NY (MSS)
Maui, HI (OGG)
Mcallen, TX (MFE)
Mccook, NE (MCK)
Mcgrath, AK (MCG)
Medford, OR (MFR)
Mekoryuk, AK (MYU)
Melbourne, FL (MLB)
Memphis, TN (MEM)
Merced, CA (MCE)
Meridian, MS (MEI)
Metlakatla, AK (MTM)
Meyers Chuck, AK (WMK)
Miami, FL - International (MIA)
Miami, FL - Sea Plane Base (MPB)
Midland, MI (MBS)
Midland/Odessa, TX (MAF)
Miles City, MT (MLS)
Milwaukee, WI (MKE)
Minneapolis, MN (MSP)
Minot, ND (MOT)
Minto, AK (MNT)
Mission, TX (MFE)
Missoula, MT (MSO)
Moab, UT (CNY)
Mobile, AL (MOB)
Modesto, CA (MOD)
Moline, IL (MLI)
Monroe, LA (MLU)
Monterey, CA (MRY)
Montgomery, AL (MGM)
Montrose, CO (MTJ)
Morgantown, WV (MGW)
Moses Lake, WA (MWH)
Mountain Home, AR (WMH)
Mountain Village, AK (MOU)
Muscle Shoals, AL (MSL)
Muskegon, MI (MKG)
Myrtle Beach, SC (MYR)
Nantucket, MA (ACK)
Napakiak, AK (WNA)
Napaskiak, AK (PKA)
Naples, FL (APF)
Nashville, TN (BNA)
Naukiti, AK (NKI)
Nelson Lagoon, AK (NLG)
New Chenega, AK (NCN)
New Haven, CT (HVN)
New Koliganek, AK (KGK)
New London/Groton (GON)
New Orleans, LA (MSY)
New Stuyahok, AK (KNW)
New York, NY - All airports (NYC)
New York, NY - Kennedy (JFK)
New York, NY - La Guardia (LGA)
Newark, NJ (EWR)
Newburgh/Stewart Field, NY (SWF)
Newport News, VA (PHF)
Newtok, AK (WWT)
Nightmute, AK (NME)
Nikolai, AK (NIB)
Nikolski, AK (IKO)
Noatak, AK (WTK)
Nome, AK (OME)
Nondalton, AK (NNL)
Noorvik, AK (ORV)
Norfolk, NE (OFK)
Norfolk, VA (ORF)
North Bend, OR (OTH)
North Platte, NE (LBF)
Northway, AK (ORT)
Nuiqsut, AK (NUI)
Nulato, AK (NUL)
Nunapitchuk, AK (NUP)
Oakland, CA (OAK)
Odessa/Midland, TX (MAF)
Ogdensburg, NY (OGS)
Oklahoma City, OK (OKC)
Omaha, NE (OMA)
Ontario, CA (ONT)
Orange County, CA (SNA)
Orlando, FL - Herndon (ORL)
Orlando, FL - International (MCO)
Oshkosh, WI (OSH)
Ottumwa, IA (OTM)
Owensboro, KY (OWB)
Oxnard/Ventura, CA (OXR)
Paducah, KY (PAH)
Page, AZ (PGA)
Palm Springs, CA (PSP)
Panama City, FL (PFN)
Parkersburg, WV/Marietta, OH (PKB)
Pasco, WA (PSC)
Pedro Bay, AK (PDB)
Pelican, AK (PEC)
Pellston, MI (PLN)
Pendleton, OR (PDT)
Pensacola, FL (PNS)
Peoria, IL (PIA)
Perryville, AK (KPV)
Petersburg, AK (PSG)
Philadelphia, PA - International (PHL)
Philadelphia, PA - Trenton/Mercer NJ (TTN)
Phoenix, AZ (PHX)
Pierre, SD (PIR)
Pilot Point, AK - Ugashnik Bay (UGB)
Pilot Point, AK (PIP)
Pilot Station, AK (PQS)
Pittsburgh, PA (PIT)
Platinum, AK (PTU)
Plattsburgh, NY (PLB)
Pocatello, ID (PIH)
Point Baker, AK (KPB)
Point Hope, AK (PHO)
Point Lay, AK (PIZ)
Ponca City, OK (PNC)
Ponce, Puerto Rico (PSE)
Port Alsworth, AK (PTA)
Port Angeles, WA (CLM)
Port Arthur/Beaumont, TX (BPT)
Port Clarence, AK (KPC)
Port Heiden, AK (PTH)
Port Moller, AK (PML)
Port Protection, AK (PPV)
Portage Creek, AK (PCA)
Portland, ME (PWM)
Portland, OR (PDX)
Portsmouth, NH (PSM)
Poughkeepsie, NY (POU)
Prescott, AZ (PRC)
Presque Isle, ME (PQI)
Princeton, WV (BLF)
Providence, RI (PVD)
Provincetown, MA (PVC)
Prudhoe Bay/Deadhorse, AK (SCC)
Pueblo, CO (PUB)
Pullman, WA (PUW)
Quincy, IL (UIN)
Quinhagak, AK (KWN)
Raleigh/Durham, NC (RDU)
Rampart, AK (RMP)
Rapid City, SD (RAP)
Reading, PA (RDG)
Red Devil, AK (RDV)
Redding, CA (RDD)
Redmond, OR (RDM)
Reno, NV (RNO)
Rhinelander, WI, (RHI)
Richmond, VA (RIC)
Riverton, WY (RIW)
Roanoke, VA (ROA)
Roche Harbor, WA (RCE)
Rochester, MN (RST)
Rochester, NY (ROC)
Rock Springs, WY (RKS)
Rockford, IL - Park&Ride Bus (ZRF)
Rockford, IL - Van Galder Bus (ZRK)
Rockland, ME (RKD)
Rosario, WA (RSJ)
Roswell, NM (ROW)
Ruby, AK (RBY)
Russian Mission, AK (RSH)
Rutland, VT (RUT)
Sacramento, CA (SMF)
Saginaw, MI (MBS)
Saint Cloud, MN (STC)
Saint George Island, AK (STG)
Saint George, UT (SGU)
Saint Louis, MO (STL)
Saint Mary's, AK (KSM)
Saint Michael, AK (SMK)
Saint Paul Island, AK (SNP)
Salem, OR (SLE)
Salina, KS (SLN)
Salisbury-Ocean City, MD (SBY)
Salt Lake City, UT (SLC)
San Angelo, TX (SJT)
San Antonio, TX (SAT)
San Diego, CA (SAN)
San Francisco, CA (SFO)
San Jose, CA (SJC)
San Juan, Puerto Rico (SJU)
San Luis Obispo, CA (SBP)
Sand Point, AK (SDP)
Santa Ana, CA (SNA)
Santa Barbara, CA (SBA)
Santa Fe, NM (SAF)
Santa Maria, CA (SMX)
Santa Rosa, CA (STS)
Saranac Lake, NY (SLK)
Sarasota, FL (SRQ)
Sault Ste Marie, MI, (CIU)
Savannah, GA (SAV)
Savoonga, AK (SVA)
Scammon Bay, AK (SCM)
Scottsbluff, NE (BFF)
Scottsdale, AZ (SDL)
Scranton, PA (AVP)
Seattle, WA - Lake Union SPB (LKE)
Seattle, WA - Seattle/Tacoma International (SEA)
Selawik, AK (WLK)
Seward, AK (SWD)
Shageluk, AK (SHX)
Shaktoolik, AK (SKK)
Sheffield/Florence/Muscle Shoals, AL (MSL)
Sheldon Point, AK (SXP)
Sheridan, WY (SHR)
Shishmaref, AK (SHH)
Shreveport, LA (SHV)
Shungnak, AK (SHG)
Silver City, NM (SVC)
Sioux City, IA (SUX)
Sioux Falls, SD (FSD)
Sitka, AK (SIT)
Skagway, AK (SGY)
Sleetmore, AK (SLQ)
South Bend, IN (SBN)
South Naknek, AK (WSN)
Southern Pines, NC (SOP)
Spartanburg/Greenville, SC (GSP)
Spokane, WA (GEG)
Springfield, IL (SPI)
Springfield, MO (SGF)
St Petersburg/Clearwater, FL (PIE)
State College/University Park, PA (SCE)
Staunton, VA (SHD)
Steamboat Springs, CO (SBS)
Stebbins, AK (WBB)
Stevens Point/Wausau, WI (CWA)
Stevens Village, AK (SVS)
Stewart Field/Newburgh, NY (SWF)
Stockton, CA (SCK)
Stony River, AK (SRV)
Sun Valley, ID (SUN)
Syracuse, NY (SYR)
Takotna, AK (TCT)
Talkeetna, AK (TKA)
Tallahassee, FL (TLH)
Tampa, FL (TPA)
Tanana, AK (TAL)
Taos, NM (TSM)
Tatitlek, AK (TEK)
Teller Mission, AK (KTS)
Telluride, CO (TEX)
Tenakee Springs, AK (TKE)
Terre Haute, IN (HUF)
Tetlin, AK (TEH)
Texarkana, AR (TXK)
Thief River Falls, MN (TVF)
Thorne Bay, AK (KTB)
Tin City, AK (TNC)
Togiak Village, AK (TOG)
Tok, AK (TKJ)
Toksook Bay, AK (OOK)
Toledo, OH (TOL)
Topeka, KS (FOE)
Traverse City, MI (TVC)
Trenton/Mercer, NJ (TTN)
Tucson, AZ (TUS)
Tulsa, OK (TUL)
Tuluksak, AK (TLT)
Tuntutuliak, AK (WTL)
Tununak, AK (TNK)
Tupelo, MS (TUP)
Tuscaloosa, AL (TCL)
Twin Falls, ID (TWF)
Twin Hills, AK (TWA)
Tyler, TX (TYR)
Unalakleet, AK (UNK)
Urbana/Champaign, IL (CMI)
Utica, NY (UCA)
Utopia Creek, AK (UTO)
Vail, CO - Eagle County Airport (EGE)
Vail, CO - Van service (QBF)
Valdez, AK (VDZ)
Valdosta, GA (VLD)
Valparaiso, FL (VPS)
Venetie, AK (VEE)
Ventura/Oxnard, CA (OXR)
Vernal, UT (VEL)
Victoria, TX (VCT)
Visalia, CA (VIS)
Waco, TX (ACT)
Wainwright, AK (AIN)
Wales, AK (WAA)
Walla Walla, WA (ALW)
Washington DC - All airports (WAS)
Washington DC - Dulles (IAD)
Washington DC - National (DCA)
Waterfall, AK (KWF)
Waterloo, IA (ALO)
Watertown, NY (ART)
Watertown, SD (ATY)
Wausau/Stevens Point, WI (CWA)
Wenatchee, WA (EAT)
West Palm Beach, FL (PBI)
West Yellowstone, MT (WYS)
Westchester County, NY (HPN)
Westerly, RI (WST)
Westsound, WA (WSX)
Whale Pass, AK (WWP)
White Mountain, AK (WMO)
White River, VT (LEB)
Wichita Falls, TX (SPS)
Wichita, KS (ICT)
Wilkes Barre, PA (AVP)
Williamsburg, VA (PHF)
Williamsport, PA (IPT)
Williston, ND (ISN)
Wilmington, NC (ILM)
Windsor Locks, CT (BDL)
Worcester, MA (ORH)
Worland, WY (WRL)
Wrangell, AK (WRG)
Yakima, WA (YKM)
Yakutat, AK (YAK)
Yellowstone/Cody, WY (COD)
Youngstown, OH (YNG)
Yuma, AZ (YUM)
'''

airport_codes = ['ABR', 'ABI', 'ADK', 'KKI', 'AKI', 'CAK', 'KQA', 'AUK', 'ALM', 'ALS', 'ALB', 'CVO', 'QWY', 'ABQ',
                 'WKK', 'AEX', 'AET', 'ABE', 'AIA', 'APN', 'AOO', 'AMA', 'ABL', 'AKP', 'ANC', 'AGN', 'ANI', 'ANV',
                 'ATW', 'ACV', 'ARC', 'AVL', 'HTS', 'ASE', 'AHN', 'AKB', 'ATL', 'AIY', 'ATK', 'AGS', 'AUG', 'AUS',
                 'BFL', 'BWI', 'BGR', 'BHB', 'BRW', 'BTI', 'BTR', 'MBS', 'BPT', 'ZBV', 'WBQ', 'BKW', 'BED', 'BLV',
                 'BLI', 'BJI', 'BEH', 'BET', 'ABE', 'BTT', 'BIL', 'GPT', 'BGM', 'KBC', 'BHM', 'BIS', 'BID', 'BMI',
                 'BLF', 'BOI', 'BOS', 'XHH', 'WHH', 'WBU', 'BYA', 'BWG', 'BZN', 'BFD', 'BRD', 'BWD', 'QKB', 'TRI',
                 'BKX', 'RBH', 'BRO', 'BQK', 'BKC', 'BUF', 'IFP', 'BUR', 'BRL', 'BTV', 'BTM', 'CAK', 'CGI', 'LUR',
                 'EHM', 'MDH', 'CLD', 'CNM', 'MRY', 'CPR', 'CDC', 'CID', 'CEM', 'CDR', 'CIK', 'CMI', 'CHS', 'CRW',
                 'CLT', 'CHO', 'CHA', 'CYF', 'VAK', 'CYS', 'CGX', 'CHI', 'MDW', 'ORD', 'CKX', 'CIC', 'KCG', 'KCQ',
                 'KCL', 'CZN', 'HIB', 'CHU', 'CVG', 'CHP', 'IRC', 'CLP', 'CKB', 'PIE', 'CLE', 'CVN', 'COD', 'CFA',
                 'KCC', 'CDB', 'CLL', 'COS', 'COU', 'CAE', 'CSG', 'GTR', 'CMH', 'CCR', 'CNK', 'QCE', 'CDV', 'CRP',
                 'CEZ', 'CGA', 'CEC', 'CKO', 'CUW', 'CBE', '', ' to', '', 'DFW', 'DAY', 'DAB', 'DEC', 'DRG', 'DJN',
                 'DEN', 'QWM', 'DSM', 'DTT', 'DTW', 'DVL', 'DIK', 'DLG', 'DDC', 'DHN', 'DUJ', 'DBQ', 'DLH', 'DRO',
                 'RDU', 'RDU', 'DUT', 'ABE', 'EAU', 'EDA', 'EEK', 'KKU', 'KEK', 'IPL', 'ELD', 'ELP', 'ELV', 'ELI',
                 'EKO', 'ELM', 'LYU', 'EMK', 'BGM', 'WDG', 'ERI', 'ESC', 'EUG', 'ACV', 'EUE', 'EVV', 'FAI', 'FAR',
                 'FYV', 'XNA', 'FAY', 'FLG', 'FNT', 'FLO', 'MSL', 'FNL', 'QWF', 'FOD', 'FLL', 'TBN', 'RSW', 'FSM',
                 'VPS', 'FWA', 'DFW', 'FKL', 'FAT', 'GNV', 'GUP', 'GCK', 'GYY', 'GCC', 'GGG', 'GGW', 'GDV', 'GLV',
                 'GNU', 'JGC', 'GCN', 'GFK', 'GRI', 'GJT', 'GRR', 'GPZ', 'KGX', 'GTF', 'GRB', 'GSO', 'GLH', 'PGV',
                 'GSP', 'GON', 'GPT', 'GUC', 'GST', 'HGR', 'SUN', 'HNS', 'PHF', 'HNM', 'PAK', 'CMX', 'LEB', 'HRL',
                 'MDT', 'HRO', 'BDL', 'HAE', 'HVR', 'HDN', 'HYS', 'HKB', 'HLN', 'AVL', 'HIB', 'HKY', 'GSO', 'ITO',
                 'HHH', 'HBB', 'HYL', 'HCR', 'HOM', 'HNL', 'MKK', 'HNH', 'HPB', 'HOT', 'HOU', 'HOU', 'IAH', 'HUS',
                 'HTS', 'HSV', 'HON', 'HSL', 'HYA', 'HYG', 'IDA', 'IGG', 'ILI', 'IPL', 'IND', 'INL', 'IYK', 'IMT',
                 'IWD', 'ISP', 'ITH', 'JAC', 'JAN', 'MKL', 'JAX', 'OAJ', 'JMS', 'JHW', 'JVL', 'BGM', 'TRI', 'JST',
                 'JBR', 'JLN', 'JNU', 'OGG', 'KAE', 'KNK', 'AZO', 'LUP', 'KLG', 'KAL', 'MUE', 'MCI', 'JHM', 'KXA',
                 'KUK', 'LIH', 'EAR', 'EEN', 'ENA', 'KTN', 'EYW', 'QKS', 'IAN', 'GGG', 'ILE', 'KVC', 'AKN', 'IGM',
                 'TRI', 'KPN', 'IRK', 'KVL', 'LMT', 'KLW', 'TYS', 'OBU', 'ADQ', 'KOA', 'KKH', 'KOT', 'OTZ', 'KYU',
                 'KWT', 'KWK', 'LSE', 'LAF', 'LFT', 'LCH', 'HII', 'LMA', 'LNY', 'LNS', 'LAN', 'LAR', 'LRD', 'LAS',
                 'LBE', 'PIB', 'LAW', 'LEB', 'KLL', 'LWB', 'LWS', 'LWT', 'LEX', 'LBL', 'LIH', 'LNK', 'LIT', 'LGB',
                 'GGG', 'LPS', 'LAX', 'SDF', 'NL)', 'QWF', 'LBB', 'MCN', 'MSN', 'MDJ', 'MHT', 'MHK', 'MBL', 'MKT',
                 'MLY', 'KMO', 'PKB', 'MWA', 'MQT', 'MLL', 'MVY', 'AOO', 'MCW', 'MSS', 'OGG', 'MFE', 'MCK', 'MCG',
                 'MFR', 'MYU', 'MLB', 'MEM', 'MCE', 'MEI', 'MTM', 'WMK', 'MIA', 'MPB', 'MBS', 'MAF', 'MLS', 'MKE',
                 'MSP', 'MOT', 'MNT', 'MFE', 'MSO', 'CNY', 'MOB', 'MOD', 'MLI', 'MLU', 'MRY', 'MGM', 'MTJ', 'MGW',
                 'MWH', 'WMH', 'MOU', 'MSL', 'MKG', 'MYR', 'ACK', 'WNA', 'PKA', 'APF', 'BNA', 'NKI', 'NLG', 'NCN',
                 'HVN', 'KGK', 'GON', 'MSY', 'KNW', 'NYC', 'JFK', 'LGA', 'EWR', 'SWF', 'PHF', 'WWT', 'NME', 'NIB',
                 'IKO', 'WTK', 'OME', 'NNL', 'ORV', 'OFK', 'ORF', 'OTH', 'LBF', 'ORT', 'NUI', 'NUL', 'NUP', 'OAK',
                 'MAF', 'OGS', 'OKC', 'OMA', 'ONT', 'SNA', 'ORL', 'MCO', 'OSH', 'OTM', 'OWB', 'OXR', 'PAH', 'PGA',
                 'PSP', 'PFN', 'PKB', 'PSC', 'PDB', 'PEC', 'PLN', 'PDT', 'PNS', 'PIA', 'KPV', 'PSG', 'PHL', 'TTN',
                 'PHX', 'PIR', 'UGB', 'PIP', 'PQS', 'PIT', 'PTU', 'PLB', 'PIH', 'KPB', 'PHO', 'PIZ', 'PNC', 'PSE',
                 'PTA', 'CLM', 'BPT', 'KPC', 'PTH', 'PML', 'PPV', 'PCA', 'PWM', 'PDX', 'PSM', 'POU', 'PRC', 'PQI',
                 'BLF', 'PVD', 'PVC', 'SCC', 'PUB', 'PUW', 'UIN', 'KWN', 'RDU', 'RMP', 'RAP', 'RDG', 'RDV', 'RDD',
                 'RDM', 'RNO', 'RHI', 'RIC', 'RIW', 'ROA', 'RCE', 'RST', 'ROC', 'RKS', 'ZRF', 'ZRK', 'RKD', 'RSJ',
                 'ROW', 'RBY', 'RSH', 'RUT', 'SMF', 'MBS', 'STC', 'STG', 'SGU', 'STL', 'KSM', 'SMK', 'SNP', 'SLE',
                 'SLN', 'SBY', 'SLC', 'SJT', 'SAT', 'SAN', 'SFO', 'SJC', 'SJU', 'SBP', 'SDP', 'SNA', 'SBA', 'SAF',
                 'SMX', 'STS', 'SLK', 'SRQ', 'CIU', 'SAV', 'SVA', 'SCM', 'BFF', 'SDL', 'AVP', 'LKE', 'SEA', 'WLK',
                 'SWD', 'SHX', 'SKK', 'MSL', 'SXP', 'SHR', 'SHH', 'SHV', 'SHG', 'SVC', 'SUX', 'FSD', 'SIT', 'SGY',
                 'SLQ', 'SBN', 'WSN', 'SOP', 'GSP', 'GEG', 'SPI', 'SGF', 'PIE', 'SCE', 'SHD', 'SBS', 'WBB', 'CWA',
                 'SVS', 'SWF', 'SCK', 'SRV', 'SUN', 'SYR', 'TCT', 'TKA', 'TLH', 'TPA', 'TAL', 'TSM', 'TEK', 'KTS',
                 'TEX', 'TKE', 'HUF', 'TEH', 'TXK', 'TVF', 'KTB', 'TNC', 'TOG', 'TKJ', 'OOK', 'TOL', 'FOE', 'TVC',
                 'TTN', 'TUS', 'TUL', 'TLT', 'WTL', 'TNK', 'TUP', 'TCL', 'TWF', 'TWA', 'TYR', 'UNK', 'CMI', 'UCA',
                 'UTO', 'EGE', 'QBF', 'VDZ', 'VLD', 'VPS', 'VEE', 'OXR', 'VEL', 'VCT', 'VIS', 'ACT', 'AIN', 'WAA',
                 'ALW', 'WAS', 'IAD', 'DCA', 'KWF', 'ALO', 'ART', 'ATY', 'CWA', 'EAT', 'PBI', 'WYS', 'HPN', 'WST',
                 'WSX', 'WWP', 'WMO', 'LEB', 'SPS', 'ICT', 'AVP', 'PHF', 'IPT', 'ISN', 'ILM', 'BDL', 'ORH', 'WRL',
                 'WRG', 'YKM', 'YAK', 'COD', 'YNG', 'YUM']


if __name__ == '__main__':
    for line in airport_codes_txt.split('\n'):
        airport_codes.append(line[-4:-1])
    print(airport_codes)
