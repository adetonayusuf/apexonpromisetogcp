# apexonpromisetogcp

**Strategic Data Migration and Advanced Analytics:**  
**Transforming On-Premises Infrastructure with Google Cloud Platform for Scalable, Data-Driven Insights**  

### **Introduction**  
Apex Solutions, a global leader in Financial Technology (FinTech), specializes in delivering innovative technology and business solutions to financial institutions and enterprises worldwide. With a focus on data-driven technology, the company empowers businesses through tailored solutions in finance, audit, consulting, and software development. By leveraging cutting-edge technology, Apex Solutions helps clients optimize operations, enhance decision-making, and achieve sustainable growth.  

However, the company's legacy on-premises infrastructure posed critical challenges, limiting scalability and hindering real-time, actionable insights. To address these limitations, Apex Solutions adopted Google Cloud Platform (GCP) to modernize its infrastructure, ensuring a scalable, secure, and data-driven future.  

---  
### **Business Challenges**  
Apex Solutions faced multiple systemic challenges that hindered operational efficiency and growth:  

#### **1. Scalability Constraints**  
- Legacy systems could not handle increasing workloads without significant hardware investments.  

#### **2. Data Silos**  
- Disparate systems led to inefficiencies, preventing seamless data integration and limiting comprehensive insights.  

#### **3. Security Concerns**  
- Maintaining robust data security and compliance was complex and resource-intensive.  

#### **4. High Maintenance Costs**  
- Frequent upgrades and ongoing maintenance diverted resources away from innovation.  

With expanding data volumes and growing operational complexity, Apex’s legacy infrastructure lacked the flexibility to adapt to evolving business and technological needs. This resulted in inefficiencies, operational defects, and constraints in generating real-time insights.  

---  
### **Data Dictionary**  
To support the migration and transformation process, Apex Solutions structured its data using the following key tables:  

#### **1. Customer Data Table**  
Stores detailed information about customers to enable analytics, personalization, and CRM insights.  
| Column Name | Data Type | Description |  
|-------------|------------|-------------|  
| Customer_ID | INT (PK) | Unique identifier for each customer. |  
| Name | VARCHAR(100) | Full name of the customer. |  
| Email | VARCHAR(255) | Contact email address of the customer. |  
| Phone | VARCHAR(15) | Contact phone number of the customer. |  
| Country | VARCHAR(100) | Country where the customer is located. |  
| Industry | VARCHAR(100) | Industry to which the customer belongs. |  
| Signup_Date | DATE | Date when the customer signed up. |  
| Last_Interaction_Date | DATE | Date of the customer's last interaction. |  

#### **2. Product Data Table**  
Stores information about the products or services offered by Apex Solutions.  
| Column Name | Data Type | Description |  
|-------------|------------|-------------|  
| Product_ID | INT (PK) | Unique identifier for each product or service. |  
| Product_Name | VARCHAR(100) | Name of the product or service. |  

#### **3. Region Data Table**  
Stores information about geographic regions where customers or sales occur.  
| Column Name | Data Type | Description |  
|-------------|------------|-------------|  
| Region_ID | INT (PK) | Unique identifier for each region. |  
| Country | VARCHAR(100) | Country associated with the region. |  
| Region_Name | VARCHAR(100) | Name of the region. |  

#### **4. Transactions Table**  
Tracks sales data to analyze revenue, trends, and customer behavior.  
| Column Name | Data Type | Description |  
|-------------|------------|-------------|  
| Transaction_ID | INT (PK) | Unique identifier for each transaction. |  
| Customer_ID | INT (FK) | Links to the Customer Data Table. |  
| Region_ID | INT (FK) | Links to the Region Data Table. |  
| Product_ID | INT (FK) | Links to the Product or Service Data Table. |  
| Transaction_Date | DATE | Date when the transaction occurred. |  
| Amount | DECIMAL(10,2) | Total revenue generated from the transaction in USD. |  
| Discount_Offered | DECIMAL(10,2) | Discount applied to the transaction, if any. |  
| Payment_Method | VARCHAR(50) | Payment method used (e.g., credit card, bank transfer). |  
| Pricing_Model | VARCHAR(50) | Pricing structure (e.g., subscription, one-time fee). |  

---  
### **The GCP Solution**  
Apex Solutions migrated to Google Cloud Platform to address these challenges and drive business transformation.  

#### **1. Scalability & Cost Optimization**  
- On-demand resource allocation ensures scalability.  
- GCP’s pay-as-you-go model reduces financial overhead.  

#### **2. Enhanced Data Integration**  
- Centralizing data on GCP eliminates silos, enabling seamless analytics.  
- Tools like Cloud Data Fusion facilitate efficient data integration.  

#### **3. Real-Time Analytics**  
- Advanced data transformation ensures accuracy and consistency.  
- BigQuery and Cloud Data Fusion drive real-time insights.  

#### **4. Improved Security & Compliance**  
- IAM roles, encryption, and audit mechanisms ensure robust data protection.  

---  
### **Implementation Strategy & Terraform Code**  

#### **1. Provisioning GCP Resources with Terraform**  
Below is the Terraform script to provision all required GCP resources, including Compute Engine, Cloud Storage, BigQuery, IAM roles, and networking components:  

  ![Main.tf](https://github.com/adetonayusuf/apexonpromisetogcp/blob/main/main.tf)

- **Loading CSV files into Google Cloud Storage (GCS)**
  ![csv_bucket.py](https://github.com/adetonayusuf/apexonpromisetogcp/blob/main/csv_bucket.py)
  
- **Loading PostgreSQL data into BigQuery**
  ![postgres-bucket-bq.py](https://github.com/adetonayusuf/apexonpromisetogcp/blob/main/postgres-bucket-bq.py)

- **Checked the integrity of the data loaded into BigQuery**
  I ran the queries below to confirm if the tables have been loaded correctly
    - The query below check for missing rows
      SELECT * 
      FROM `apexgcp.apex_dataset.transactions`
      WHERE Customer_ID IS NULL OR Transaction_ID IS NULL;

    - The query below is to indentify if there's any duplicate in the transactions table
      SELECT Transaction_ID, COUNT(*) 
      FROM `apexgcp.apex_dataset.transactions`
      GROUP BY Transaction_ID
      HAVING COUNT(*) > 1;

  
  
- **Transforming data using dbt (data build tool)**
  Transforming the raw data in BigQuery to analytics-ready datasets with the help of dbt. After setting up dbt for the project, docker scripts were generated.
    ![dbt_project.yml](https://github.com/adetonayusuf/apexonpromisetogcp/blob/main/dbt_project.yml)
    ![schema.yml](https://github.com/adetonayusuf/apexonpromisetogcp/blob/main/schema.yml)
    ![sources.yml](https://github.com/adetonayusuf/apexonpromisetogcp/blob/main/sources.yml)

  Then i created staging folders were all the SQL queries that will be used to reform my tables that will be eventually used to create a new transformed transaction tables   that will be used for analysis.
    ![stg_customers.sql](https://github.com/adetonayusuf/apexonpromisetogcp/blob/main/stg_customers.sql)
    ![stg_products.sql](https://github.com/adetonayusuf/apexonpromisetogcp/blob/main/stg_products.sql)
    ![stg_regions.sql](https://github.com/adetonayusuf/apexonpromisetogcp/blob/main/stg_regions.sql)
    ![stg_transactions.sql](https://github.com/adetonayusuf/apexonpromisetogcp/blob/main/stg_transactions.sql)

  Then a created core_mart folder that house the transformed dataset that will be use for analysis
    ![core_transaction_analysis.sql](https://github.com/adetonayusuf/apexonpromisetogcp/blob/main/core_transaction_analysis.sql)
 
- **Ensuring data integrity and implementing security measures**

---  
### **Conclusion**  
Apex Solutions' transition to Google Cloud Platform marked a significant step toward achieving scalable, secure, and data-driven operations. By leveraging cloud-native tools and advanced analytics, the company successfully optimized its infrastructure, reduced costs, and enhanced real-time decision-making capabilities. This transformation underscores the importance of cloud adoption in driving business growth and innovation.

