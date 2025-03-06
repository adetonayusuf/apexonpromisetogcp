
# **apexonpromisetogcp**

## **Transforming On-Premises Infrastructure with Google Cloud Platform for Scalable, Data-Driven Insights**

### **Introduction**
Apex Solutions, a global leader in Financial Technology (FinTech), specializes in delivering innovative technology and business solutions to financial institutions and enterprises worldwide. With a focus on data-driven technology, the company empowers businesses through tailored solutions in finance, audit, consulting, and software development. By leveraging cutting-edge technology, Apex Solutions helps clients optimize operations, enhance decision-making, and achieve sustainable growth.

However, the company's legacy on-premises infrastructure posed critical challenges, limiting scalability and hindering real-time, actionable insights. To address these limitations, Apex Solutions adopted **Google Cloud Platform (GCP)** to modernize its infrastructure, ensuring a scalable, secure, and data-driven future.

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
Apex Solutions migrated to **Google Cloud Platform (GCP)** to address these challenges and drive business transformation.

#### **1. Scalability & Cost Optimization**
- On-demand resource allocation ensures scalability.
- GCP’s pay-as-you-go model reduces financial overhead.

#### **2. Enhanced Data Integration**
- Centralizing data on GCP eliminates silos, enabling seamless analytics.
- Tools like **Cloud Data Fusion** facilitate efficient data integration.

#### **3. Real-Time Analytics**
- Advanced data transformation ensures accuracy and consistency.
- **BigQuery** and **Cloud Data Fusion** drive real-time insights.

#### **4. Improved Security & Compliance**
- IAM roles, encryption, and audit mechanisms ensure robust data protection.

---

Below is the data Architecture for this project

![Data Architecture](https://github.com/adetonayusuf/apexonpromisetogcp/blob/main/GCP%20Architecture.png)

---
### **Technology Stack**
- **Cloud Platform**: Google Cloud Platform (BigQuery, Cloud Storage, Dataflow, AI Platform)
- **Infrastructure as Code Tools**: Terraform
- **Data Integration Tools**: Cloud Data Fusion
- **Analytics Tools**: Looker, BigQuery
- **Data Transformation Tools**: dbt (data build tool)
- **Security Solutions**: Cloud Identity and Access Management (IAM)
- **Programming Languages**: Python, SQL

---
### **Data Source**
The source data for this project includes CSV and dump files. The data was initially loaded into **PostgreSQL** and later imported into **Google Cloud Storage (GCS) and BigQuery**.

---
### **Implementation Strategy & Terraform Code**

#### **1. Provisioning GCP Resources with Terraform**  
- Terraform script: [main.tf](https://github.com/adetonayusuf/apexonpromisetogcp/blob/main/main.tf)

#### **2. Loading CSV files into Google Cloud Storage (GCS)**  
- Python script: [csv_bucket.py](https://github.com/adetonayusuf/apexonpromisetogcp/blob/main/csv_bucket.py)

#### **3. Loading PostgreSQL Data into BigQuery**  
- Python script: [postgres-bucket-bq.py](https://github.com/adetonayusuf/apexonpromisetogcp/blob/main/postgres-bucket-bq.py)

#### **4. Data Integrity Checks in BigQuery**
- Queries to check missing or duplicate records.
    - The query below check for missing rows

       SELECT * 
       FROM `apexgcp.apex_dataset.transactions`
      WHERE Customer_ID IS NULL OR Transaction_ID IS NULL;

  - The query below is to indentify if there's any duplicate in the transactions table
    
      SELECT Transaction_ID, COUNT(*) 
      FROM `apexgcp.apex_dataset.transactions`
      GROUP BY Transaction_ID
      HAVING COUNT(*) > 1;

#### **5. Data Transformation with dbt**
- Staging SQL scripts: [stg_customers.sql](https://github.com/adetonayusuf/apexonpromisetogcp/blob/main/stg_customers.sql)
                       [stg_products.sql](https://github.com/adetonayusuf/apexonpromisetogcp/blob/main/stg_products.sql)
                       [stg_regions.sql](https://github.com/adetonayusuf/apexonpromisetogcp/blob/main/stg_regions.sql)
                       [stg_transactions.sql](https://github.com/adetonayusuf/apexonpromisetogcp/blob/main/stg_transactions.sql)
- Core_mart Script:    ![core_transaction_analysis.sql](https://github.com/adetonayusuf/apexonpromisetogcp/blob/main/core_transaction_analysis.sql)

#### **6. Automating Pipelines with Cloud Composer (Airflow)**
- DAG setup and execution in Airflow.
    Python Script: [wk-airflow.py](https://github.com/adetonayusuf/apexonpromisetogcp/blob/main/wk-airflow.py)

#### **7. Google Looker - GCP Transaction Analysis**
- Dashboard visualization: [Transaction Analysis](https://github.com/adetonayusuf/apexonpromisetogcp/blob/main/GCP%20Transaction%20Analysis.png)

#### **8. Power BI - GCP Transaction Analysis**
- Dashboards analyzing **Gross Revenue, Net Revenue, Discounts, COGS, and Gross Profit**.
    - Power BI Dashboard visualization: [Gross Revenue.png](https://github.com/adetonayusuf/apexonpromisetogcp/blob/main/Gross%20Revenue.png)
                                        [Discount.png](https://github.com/adetonayusuf/apexonpromisetogcp/blob/main/Discount.png)
                                        [Net Revenue.png](https://github.com/adetonayusuf/apexonpromisetogcp/blob/main/Net%20Revenue.png)
                                        [COGS.png](https://github.com/adetonayusuf/apexonpromisetogcp/blob/main/COGS.png)
                                        [Gross Profit.png](https://github.com/adetonayusuf/apexonpromisetogcp/blob/main/Gross%20Profit.png)                                        

### **Conclusion**
Apex Solutions' transition to **Google Cloud Platform (GCP)** marked a significant step toward achieving **scalable, secure, and data-driven operations**. By leveraging cloud-native tools and advanced analytics, the company successfully optimized its infrastructure, reduced costs, and enhanced real-time decision-making capabilities. This transformation underscores the importance of cloud adoption in driving business growth and innovation.
