import copy

class CityAnalyzer:
    def __init__(self):
        self.cityData = []
        self.processed_data = []
        
    def load_data(self, filename="dataset.csv"):
        with open(filename, "r") as cityDataFile:
            self.cityData = cityDataFile.readlines()
            self._process_raw_data()
            
    def _process_raw_data(self):
        for i in range(len(self.cityData)):
            if i == 0: continue
            self.cityData[i] = self.cityData[i].split(";")
            avg_income = self.cityData[i][1]
            
            # Process each field
            self.cityData[i][0] = self.cityData[i][0].strip()  # City
            self.cityData[i][1] = float(self.cityData[i][1][1:-1])  # Average income
            self.cityData[i][2] = float(self.cityData[i][2])  # Education
            self.cityData[i][3] = float(self.cityData[i][3])  # Density
            self.cityData[i][4] = int(self.cityData[i][4])    # Population
            self.cityData[i][5] = int(self.cityData[i][5])    # Pollution
            self.cityData[i][6] = float(self.cityData[i][6])  # Crime rate
            self.cityData[i][7] = float(self.cityData[i][7])  # Latitude
            self.cityData[i][8] = float(self.cityData[i][8].strip())  # Longitude
            self.cityData[i][9] = self.cityData[i][9].strip() # Sentence
            
            # Add picture name and original average income
            self.cityData[i].append(self.cityData[i][0].replace(" ", "_")+".jpg")
            self.cityData[i].append(avg_income)
            
        del(self.cityData[0])
        
    def _reformat(self, list0):
        dif = abs(max(list0) - min(list0))
        return [(x - min(list0)) / dif * 100 for x in list0]
    
    def normalize_data(self):
        CityData = copy.deepcopy(self.cityData)
        
        # Extract and normalize each metric
        metrics = [[] for _ in range(6)]
        for city in CityData:
            for i in range(6):
                metrics[i].append(city[i+1])
                
        # Apply normalization
        for i, metric in enumerate(metrics):
            normalized = self._reformat(metric)
            for j in range(len(CityData)):
                CityData[j][i+1] = normalized[j]
                
        return CityData
    
    def calculate_scores(self, normalized_data, weights):
        scoreData = []
        coefficient = [w/sum(weights) for w in weights]
        
        for city_data in normalized_data:
            score = sum(coef * value for coef, value in zip(coefficient, city_data[1:7]))
            scoreData.append([score, city_data])
            
        return sorted(scoreData, reverse=True)
    
    def prepare_output_data(self, scored_data, num_cities=15):
        output_data = []
        for i in range(min(num_cities, len(scored_data))):
            city = scored_data[i][1]
            output_data.append([
                city[0],    # City name
                city[7],    # latitude
                city[8],    # longitude
                city[11],   # Average income
                city[4],    # Population
                round(city[6], 3),  # Crime rate
                city[9],    # Sentence
                city[10],   # Picture name
                f"https://en.wikipedia.org/wiki/{city[0].replace(' ', '_')}"  # Website
            ])
        
        # Transpose data for display
        return [[row[i] for row in output_data] for i in range(len(output_data[0]))]
    
    def analyze_cities(self, user_preferences):
        normalized_data = self.normalize_data()
        scored_data = self.calculate_scores(normalized_data, user_preferences)
        return self.prepare_output_data(scored_data)