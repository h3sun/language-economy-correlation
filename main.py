# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %%
def load_language_codes(file_path: str) -> pd.DataFrame:
    """
    Load language codes dataset from tab-separated file.
    
    Args:
        file_path (str): Path to the LanguageCodes.tab.txt file
        
    Returns:
        pd.DataFrame: DataFrame containing language codes data
    """
    try:
        # Load tab-separated file
        language_codes = pd.read_csv(file_path, sep='\t')
        
        print(f"Successfully loaded language codes dataset")
        print(f"Dataset shape: {language_codes.shape}")
        print(f"Columns: {language_codes.columns.tolist()}")
        
        return language_codes
        
    except FileNotFoundError:
        print(f"Error: File {file_path} not found")
        return pd.DataFrame()
    except Exception as e:
        print(f"Error loading file: {e}")
        return pd.DataFrame()

# Load country ISO codes dataset

# %%
# Load dataset country_iso_codes and country_gdp
country_iso_codes = pd.read_csv('dataset/country-iso-codes.csv')
country_gdp = pd.read_csv('dataset/CountryGdp.csv')

# %%
# Load dataset language_codes

# Load language codes dataset
language_codes = load_language_codes('dataset/LanguageCodes.tab.txt')

# %%
language_codes

# %%
# Group language codes by country to count languages per country
def count_languages_per_country(language_df: pd.DataFrame) -> pd.DataFrame:
    """
    Count the number of languages per country from language codes dataset.
    
    Args:
        language_df (pd.DataFrame): DataFrame containing language codes data
        
    Returns:
        pd.DataFrame: DataFrame with country codes and language counts
    """
    if language_df.empty:
        print("Error: Empty language codes dataset")
        return pd.DataFrame()
    
    # Group by CountryID and count unique languages
    languages_per_country = language_df.groupby('CountryID').agg({
        'LangID': 'count',  # Count total languages
        'Name': 'nunique'   # Count unique language names
    }).reset_index()
    
    # Rename columns for clarity
    languages_per_country.columns = ['CountryID', 'Total_Languages', 'Unique_Languages']
    
    # Sort by number of languages (descending)
    languages_per_country = languages_per_country.sort_values('Total_Languages', ascending=False)
    
    print("Languages per country (top 20):")
    print(languages_per_country.head(20))
    
    print(f"\nSummary statistics:")
    print(f"Total countries: {len(languages_per_country)}")
    print(f"Average languages per country: {languages_per_country['Total_Languages'].mean():.2f}")
    print(f"Median languages per country: {languages_per_country['Total_Languages'].median():.2f}")
    print(f"Max languages in a country: {languages_per_country['Total_Languages'].max()}")
    print(f"Min languages in a country: {languages_per_country['Total_Languages'].min()}")
    
    return languages_per_country

# Count languages per country
languages_per_country = count_languages_per_country(language_codes)

# %%
languages_per_country
country_iso_codes
country_gdp 
# %%
country_name_list = []
country_gdp_list = []
country_languages_list = []
gdp_per_capita_list = []
population_list = []
for alpha_2_code in country_iso_codes['Alpha-2 code']:
    try:
        single_country_name = country_iso_codes[country_iso_codes['Alpha-2 code'] == alpha_2_code]['English short name lower case'].values[0]
        single_country_gdp = country_gdp[country_gdp['Country'] == single_country_name]['UN_GDP'].values[0]
        single_gdp_per_capita = country_gdp[country_gdp['Country'] == single_country_name]['GDP_per_capita'].values[0]
        single_population = country_gdp[country_gdp['Country'] == single_country_name]['Population'].values[0]
        single_country_languages = languages_per_country[languages_per_country['CountryID'] == alpha_2_code]['Total_Languages'].values[0]

        print(single_country_name, single_country_gdp, single_country_languages, single_gdp_per_capita)
        country_name_list.append(single_country_name)
        country_gdp_list.append(single_country_gdp)
        country_languages_list.append(single_country_languages)
        gdp_per_capita_list.append(single_gdp_per_capita)
        population_list.append(single_population)
    except Exception as e:
        print(f"Error: {e}")

# %%
# Find the covariance between country_gdp_list and country_languages_list

# Variance

def compute_variance(arr):
    if not arr or len(arr) == 0:
        return 0
    mean = np.mean(arr)
    var = 0
    for num in arr:
        var = var + (num - mean) ** 2
    
    return var / len(arr)


def compute_covariance(arr1, arr2):
    if not arr1 or not arr2 or len(arr1) != len(arr2):
        return 0
    mean1 = np.mean(arr1)
    mean2 = np.mean(arr2)
    covariance = 0
    for i in range(len(arr1)):
        covariance += (arr1[i] - mean1) * (arr2[i] - mean2)
    return covariance / len(arr1)

def compute_correlation(arr1, arr2):
    variance1 = compute_variance(arr1)
    variance2 = compute_variance(arr2)
    covariance = compute_covariance(arr1, arr2)
    return covariance / np.sqrt(variance1 * variance2)

compute_correlation(country_gdp_list, country_languages_list)
# %%
# Compute correlation using numpy
print("Correlation between country_gdp_list and country_languages_list: ", np.corrcoef(country_gdp_list, country_languages_list)[0, 1])
print("Correlation between country_gdp_list and gdp_per_capita_list: ", np.corrcoef(country_gdp_list, gdp_per_capita_list)[0, 1])
print("Correlation between country_gdp_list and population_list: ", np.corrcoef(country_gdp_list, population_list)[0, 1])
# %%

country_gdp
# %%
