**Photovoltaic-battery integration strategy in plant factories with artificial lighting**

***Thomas Xiong1, Wenyi Cai1, Yue Hu2, Mengxuan Song3, TingTing Qian4\*, Hua Bao1\****

1Global Institute of Future Technology, Shanghai Jiao Tong University, Shanghai 200240, China

2CTG Wuhan Science and Technology Innovation Park, China Three Gorges Corporation, Wuhan 430010, China

3School of Energy and Materials, Shanghai Polytechnic University, Shanghai 201209, China

4Agricultural Information Institute of Science and Technology, Shanghai Academy of Agricultural Sciences, Shanghai 201403, China

# ABSTRACT

Plant Factories with Artificial Lighting (PFALs) offer sustainable food production but face high energy costs that hinder their widespread adoption as a novel building-integrated agriculture solution. Photovoltaic-battery energy storage systems (PVBES) can substantially reduce these costs, addressing a primary barrier to PFAL scalability. However, current research generally adopts a passive integration strategy, overlooking the unique temporal flexibility of artificial lighting schedules. Furthermore, there is a lack of established design benchmarks regarding the specific PVBES configurations required for energy-autonomous container PFALs. Here, we propose a sizing-scheduling coordination strategy that jointly optimizes photovoltaic array sizes, battery capacities, and photoperiod schedules. This approach shifts PFAL energy management from rigid load coverage to active sizing-scheduling coordination. First, based on year-round experimental monitoring, we found that a typical 20-foot container PFAL (16 m2 cultivation area) requires distinct PVBES configurations by region. Typical conditions in Shanghai would require a minimum of 80 m2 PV array area and 50 kWh BES capacity. Notably, our analysis shows that aligning LED loads with solar availability reduces BES capacity needs by up to 40% to achieve near-energy autonomy. Economic analysis shows that optimized PFAL-PVBES configurations can cut electricity costs by 57-67% compared to grid prices and reduce grid dependency by 59.4-92.8%. More generally, locations with high solar resources and colder temperatures are the most favorable for integrating PVBES into PFALs. Finally, we released our findings through an open-source framework (OpenCROPS) to invite researchers and practitioners to improve PFAL-PVBES modeling further and tailor their specific solutions.

**KEYWORDS**: Plant factory with artificial lighting; Photovoltaic-battery energy storage system; Sizing-scheduling coordination; Photoperiod scheduling; Techno-economic analysis

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\*Corresponding authors.

*E-mail addresses:* hua.bao@sjtu.edu.cn (H. Bao), qiantingting@saas.sh.cn (T. Qian)

**Nomenclature Table**

|  |  |
| --- | --- |
| **Abbreviations** | |
| BES | Battery Energy Storage |
| COP | Coefficient Of Performance |
| GD | Grid Dependency |
| LCOE | Levelized Cost of Energy |
| LED | Light-Emitting Diode |
| PBP | Payback Period |
| PFAL | Plant Factory with Artificial Lighting |
| PV | Photovoltaic |
| PVBES | Photovoltaic Battery Energy Storage System |
| **Symbols** | |
| **Economic Parameters** | |
|  | Total capital cost [$] |
|  | Electricity produced in year t [kWh] |
|  | Grid electricity cost in year t [$] |
|  | Investment in year t [$] |
|  | Maintenance and operation cost in year t [$·year-1] |
|  | System lifetime [years] |
|  | Discount rate [dimensionless] |
|  | Annual savings compared to grid-only operation [$] |
| **PV System Parameters** | |
|  | Solar irradiance [W·m-2] |
|  | Solar irradiance at standard test conditions (1000 W·m-2) |
|  | Output current [A] |
|  | Light-generated current [A] |
|  | Diode saturation current [A] |
|  | Short-circuit current at standard test conditions [A] |
|  | Boltzmann constant [J·K-1] |
|  | Number of cells in series [dimensionless] |
|  | Diode ideality factor [dimensionless] |
|  | Power [kW] |
|  | Electron charge [C] |
|  | Series resistance [Ω] |
|  | Shunt resistance [Ω] |
|  | Electricity cost savings [$] |
|  | Module temperature [°C] |
|  | Reference temperature (25°C) |
|  | Output voltage [V] |
|  | Open-circuit voltage [V] |
|  | Open-circuit voltage at standard test conditions [V] |
|  | Thermal voltage [V] |
|  | Temperature coefficient for short-circuit current [A·°C-1] |
|  | Temperature coefficient for open-circuit voltage [%·°C-1] |
| **Battery System Parameters** | |
|  | BES capacity [kWh] |
|  | Battery energy at time t [kWh] |
|  | Charging power at time t [kW] |
|  | Discharging power at time t [kW] |
|  | Minimum state of energy [dimensionless] |
|  | Time Loss of Power Supply [%] |
|  | Maximum allowable Time Loss of Power Supply [%] |
|  | Battery installation capacity [kWh] |
|  | Time interval [h] |
|  | Charging efficiency [dimensionless] |
|  | Discharging efficiency [dimensionless] |
|  | Power shortage indicator [binary] |
| **Accuracy Metrics** | |
|  | Coefficient of variation of the root mean square error |
|  | Normalized mean square error |
|  | Coefficient of determination |
| **Subscripts** | |
| *ann* | Annual |
| *bat* | Battery |
| *cap* | Capital |
| *ch* | Charging |
| *dch* | Discharging |
| *grid* | Utility grid |
| *inv* | Inverter |
| *max* | Maximum |
| *min* | Minimum |
| *oc* | Open circuit |
| *opt* | Optimal |
| *p* | Peak |
| *sc* | Short circuit |
| *stc* | Standard test conditions |
| *th* | Thermal |
| *tot* | Total |

# 1. Introduction

Recent extreme climate events and pandemics have underscored vulnerabilities in global food supply chains, prompting a shift toward resilient, localized food production systems [1,2]. This trend has accelerated the adoption of Controlled-Environment Agriculture (CEA), with Plant Factories with Artificial Lighting (PFALs) emerging as highly effective, special-purpose buildings that enable year-round crop production regardless of external climate conditions [3,4,5]. However, the controlled environment within PFALs requires substantial electricity inputs for Light-Emitting Diode (LED) lighting to artificially stimulate photosynthesis in buildings and air conditioning units to manage massive internal heat gains [5,6,7,8,9,10]. This energy intensity translates directly into operational economics, with electricity costs accounting for 30%-50% of total operational expenses [4,5,11,12]. Consequently, addressing the energy cost challenge is imperative to enhance the economic viability and scalability of PFALs for sustainable food production.

There are two main directions in prior research to reduce energy costs in PFALs. The first direction is to lower energy costs by reducing energy consumption in PFALs. At the system level, studies employed simulation to identify and optimize key factors influencing energy consumption, such as the coefficient of performance (COP) of air-conditioning units, LED efficiency, and envelope heat transfer coefficients [6,13,14]. At the component level, innovations such as air-side economizers and smart controllers are explored to reduce air-conditioning energy consumption [7,8,15]. Other studies have explored methods to reduce LED energy consumption through dynamic control, reflective films, and pulsed-frequency lighting [10,11,16].

The second direction to reduce energy costs in PFALs is to explore solar power. Recently, the integration of Photovoltaic (PV) technology coupled with Battery Energy Storage Systems (BES), collectively termed PVBES, has gained growing interest as a cost-effective solution to enhance energy sustainability in CEA [17-20]. Beyond agriculture, PVBES has seen widespread applications in diverse fields [21-24]. In residential and industrial microgrids, optimization approaches typically focus on sizing components to minimize the Levelized Cost of Energy (LCOE) or maximize self-consumption. For instance, studies in these sectors [21,24] have established robust methodologies for jointly optimizing generation and storage capacity, often using demand-side management to align flexible loads with solar availability.

Within the context of CEA [25-27], research can be categorized into three directions. First, studies have demonstrated that PVBES can offset energy consumption in greenhouses while supporting crop production [28-30]. For instance, Hu et al. reported that PV systems offset 25.7% of the energy demand of a greenhouse [30]. In comparison, Naghibi et al. optimized a hybrid PVBES and solar thermal system covering 51% of the electricity load [31]. Economic analyses further confirm the viability of PVBES in greenhouses [32-34], with Marucci et al. reporting payback periods as low as six years [32] and Li et al. noting ranges of four to eight years [33]. However, these greenhouse-oriented studies typically treat the load profile as a weather-dependent variable driven by heating and cooling needs, which cannot be significantly shifted. As for progress in PFALs, studies have primarily focused on PV systems without integrating BES [35-39]. For instance, Li et al. reported that a PFAL combined with PV could provide better economic sustainability than a standalone configuration in tropical cities [27]. Jiang et al. achieved an energy-saving rate of 4.31% by integrating PV in an experimental setup [38]. While these studies demonstrate the feasibility of PV for reducing energy costs in PFALs, they generally adopt a "passive" integration strategy. They treat energy system sizing based on a fixed, predetermined PFAL load profile rather than applying advanced active load coordination strategies from the broader microgrid literature [21,24].

Despite these advancements, current research on PVBES in PFALs faces two critical limitations. First, existing approaches overlook the temporal flexibility of artificial lighting schedules. Unlike inflexible loads in conventional buildings, the photoperiod in PFALs can be shifted without compromising crop yield [40]. However, current studies treat it as a fixed temporal pattern, failing to exploit this unique degree of freedom for active load coordination. Second, there is a lack of established design guidelines regarding the specific PVBES configurations required to achieve energy autonomy for typical production units, specifically the widely used 20-foot shipping container PFALs [3]. Consequently, a systematic strategy is needed to jointly optimize photoperiod timing and PVBES capacity. This work addresses these gaps by shifting the design paradigm from passive component sizing to active sizing-scheduling coordination. Specifically, we aim to: (1) quantify the operational benefits of dynamically aligning the photoperiod with daily solar availability to minimize storage needs, and (2) establish the techno-economic feasibility boundaries and optimal sizing benchmarks required to support the high energy demands of container PFALs under diverse climate conditions.

To address this gap, we systematically optimize PFAL-PVBES integration by jointly modeling PV generation, BES operation, and PFAL load profiles. We first monitored and analyzed the energy consumption of a 20-foot container PFAL for a whole year. These experimental data allow us to simulate the energy patterns in a PFAL-PVBES system. Then, we identified minimal PFAL-PVBES system configurations that achieve energy autonomy tailored to diverse climate conditions. Next, by setting economic metrics as objectives, we optimized PVBES and photoperiod combinations to demonstrate the potential for reducing energy costs in PFALs. Finally, as an additional contribution to the field, we uploaded our framework and data to an open-source repository to ensure reproducibility and facilitate future research.

# 2. Methodology

This section presents the technical roadmap and modeling approach for the PFAL-PVBES optimization framework. As illustrated in Fig. 1, we first present the experimental data monitored from a container PFAL and simulate it using EnergyPlus (Section 2.1) at level 1. Then we build models for both the PV and BES components, which allow us to more accurately simulate the PFAL-PVBES system and construct the level 2 (Section 2.2). Then we present the optimization workflow for efficient PFAL-PVBES system design (Section 2.3) to build the level 3. In Section 2.4, we complement level 1 with detailed specifications for specific PFAL-PVBES. Finally, the evaluation level 4 will be conducted in the results section.

![picture](data:image/png;base64...)

Fig. 1. Overview of the integrated simulation and optimization framework for the PFAL-PVBES system. The framework is structured into four hierarchical levels: (1) Case Study Setup, which integrates local weather data with the EnergyPlus thermal model; (2) Hybrid Modeling, simulating the dynamic energy flow between PFAL loads, PV generation, and battery storage; (3) Design Optimization, performing a parametric sweep of photoperiods and system sizing to ensure hourly energy balance; and (4) Evaluation, identifying the optimal design that minimizes the LCOE while meeting grid dependency constraints.

## 2.1 PFAL data monitoring and modeling

PFAL energy consumption depends on the climate and geographical location [12,13]. Therefore, we need to have a thorough understanding of the energy consumption dynamics in PFALs. This section details a methodology for generating location-specific PFAL load profiles using validated energy modeling techniques, enabling analysis across diverse contexts.

The energy consumption model parameters in this work are derived from the same 20-foot container-based PFAL in Shanghai, China, as established by Yu et al. [42] (see Fig. 2 (a)). Notably, many key parameters for this PFAL setup have been rigorously measured and validated in their work, ensuring robust inputs for our simulations. Energy consumption for the LED lighting, fresh air unit, fan filter unit, and air-conditioning unit was monitored using a single-phase pre-payment watt-hour meter with an accuracy of ±0.01 kWh·h-1. Envelope thermal properties include a conduction rate of 0.014 W·m-1·K-1 (measured via Testo 875 Pro infrared camera, ±2% accuracy, and JTR01 heat flux meter, ±5% accuracy), an infiltration rate of 0.9 air changes per hour, and a fresh air fan ventilation rate ranging from 0 to 12.65 air changes per hour. Equipment heat dissipation rates are verified as 0.65 for the LED system and 0.3 for the fresh air and fan filter units [42]. Additional specifications, per construction documents, encompass a solar absorptivity of 0.4 and a culture room envelope thickness of 0.05 m. Geospatial data obtained from Baidu Maps measurements indicate a latitude of 31.6 °N, a longitude of 121.5 °E, and an orientation of 22.7 ° (with the long façade facing north). These validated parameters form the foundation for the EnergyPlus model used in our following simulations.

![g:/pvbes_design/submission/v14/071610141585_0Load_A_pfal_images.png071610141585_0Load_A_pfal_images](data:image/png;base64...)

Fig. 2. Energy consumption analysis of PFAL operations. (a) Picture of the actual exemplary container PFAL. (b) Daily energy consumption of PFAL across major components (LED lighting, air-conditioning unit, fan filter unit, fresh air unit) for the whole year. (c) Average daily energy consumption by season, excluding the spring festival period. Bar chart visualization showing the distribution of energy consumption for each season, with numerical values and percentage contributions highlighting seasonal variations in energy use patterns. (d) Seasonal COP analysis of the air-conditioning system. Bar chart displaying the calculated COP values for each season.

This work further collects year-round operational data (January-December 2024) from the same PFAL under standard cultivation conditions, managed by professional growers. During year-round operation, energy consumption for the major components (LED lighting, air-conditioning unit, fan filter unit, and fresh air unit) was monitored at 1-hour intervals [42]. As shown in Figs. 2 (b) and 2 (c), total energy consumption shows seasonal variation, ranging from approximately 20 kWh·day-1 during winter months to peak values exceeding 45 kWh·day-1 during summer and early fall. The LED lighting demonstrates relatively consistent consumption patterns (10-20 kWh·day-1) with periodic adjustments corresponding to various crop production cycles. The corresponding power rate is about one-third to two-thirds of the LED full power (1.370 kW) equipped in the container PFAL. The air-conditioning units exhibit pronounced monthly variation, with minimal usage in winter months (below 5 kWh·day-1) and higher consumption during summer (up to 25 kWh·day-1). The fan and ventilation systems maintain relatively stable consumption year-round. A notable operation interruption occurred during February-March, coinciding with the Spring Festival holiday period, when the PFAL temporarily suspended operations.

The previous analysis indicates that the primary source of energy variability in PFAL is the air-conditioning system. Following the method described by Yu et al. [42], we calculated the COP of the air-conditioning unit on a seasonal basis. The following calculations excluded data from the spring festival vacation periods. Fig. 2 (d) illustrates distinct seasonal COP values: 3.94 (winter), 3.85 (spring), 2.73 (summer), and 2.57 (fall). These values are based on maintaining indoor temperatures between 18 °C and 24 °C in the PFAL during 2024. In winter and spring, lower outdoor temperatures often require heating; however, heat dissipation from LED lighting and other equipment offsets the energy demand for air conditioning, resulting in lower consumption and a higher COP. In summer and fall, outdoor temperatures often exceed indoor temperatures, requiring the air conditioner to operate in cooling mode to manage excess heat from the environment and internal equipment, thereby increasing energy consumption and lowering the COP. These seasonal COP values serve as critical inputs for the energy modeling process.

To accurately forecast building energy consumption, this work employed EnergyPlus, a validated building energy simulation program (see validation details in Fig. S1 (a)), to develop location-specific annual PFAL load profiles. To assess outdoor weather impacts on PFAL indoor environments, meteorological data are integrated using location-specific historical records (e.g., 2024) [43,44].

Following data integration, a simulation and load calculation phase is executed by running the EnergyPlus simulation. This model directly outputs energy consumption for scheduled components (LED lighting, fan filter unit, and fresh air unit) and, crucially, generates hourly thermal loads for the PFAL based on the previously mentioned container and equipment parameters. These thermal loads encompass envelope contributions, accounting for conduction from outdoor weather conditions and infiltration losses, as well as heat dissipation from equipment. Per Yu et al. [42], latent loads from plants are not a significant factor in air-conditioning energy usage. Unlike greenhouses, where plant sensible and latent heat gains arise independently, all such gains in PFALs can be attributed to the visible fraction of LED output; accordingly, latent loads are excluded here, with the LED heat dissipation fraction adjusted to 1.

A key step is then to calculate air-conditioning energy consumption by combining the simulated hourly thermal loads with the corresponding derived seasonal COP values (as shown in Fig. 1 (d)). We employ seasonal COP values primarily for their simplicity in capturing the aggregate efficiency of the air-conditioning system across diverse operating conditions throughout the year, thereby avoiding the complexity of hourly COP variations while maintaining sufficient accuracy for energy modeling. The seasonal COP assumes that the air-conditioning efficiency remains constant throughout the season. Finally, the process concludes by summing the calculated air-conditioning energy consumption with the simulated energy use of other components (LED, fan filter unit, fresh air unit) to produce a total hourly energy load profile for the entire year for the specified location and operational schedule. The applicability of this EnergyPlus model has been validated with an R2 of 0.908 (see Fig. S1(a)).

### 2.2 PVBES modeling

The PFAL-PVBES modeling framework takes direct and diffuse solar radiation as inputs and uses the single diode model to simulate the performance of PV modules [41,45,46]. The fundamental equation of the single diode model is expressed as:

![](data:image/x-wmf;base64...) (1)

where ![](data:image/x-wmf;base64...) represents the output current, ![](data:image/x-wmf;base64...) is the output voltage, ![](data:image/x-wmf;base64...) is the light-generated current, ![](data:image/x-wmf;base64...) is the diode saturation current, ![](data:image/x-wmf;base64...) is the series resistance, ![](data:image/x-wmf;base64...) is the shunt resistance, ![](data:image/x-wmf;base64...) is the diode ideality factor, ![](data:image/x-wmf;base64...) is the number of cells in series, and ![](data:image/x-wmf;base64...) is the thermal voltage. The model parameters are adjusted for environmental conditions using established relationships [41,46] (see Section 1 of the Supplementary Information for more details). Furthermore, the PV model has been validated against manufacturer experimental data, achieving an R2 of 0.992 (see Fig. S1(c)).

The PFAL-PVBES framework uses a power-flow calculation algorithm to simulate the charging and discharging dynamics of BES [41]. This process begins by calculating the current battery charge level from its previous state. The principle is that when excess PV power is available, the battery charges at the minimum of the surplus power, the remaining BES capacity, and the maximum charging rate. Conversely, during energy deficits, the battery discharges at the minimum of the required power, the available stored energy, and the maximum discharge rate. This modeling component accounts for natural battery self-discharge at each time step and maintains operation within safe state-of-charge boundaries [41]. The battery energy at any hour![](data:image/x-wmf;base64...) is calculated through the equation proposed by Zhao et al. [41]:

![](data:image/x-wmf;base64...) (2)

Where ![](data:image/x-wmf;base64...)is the minimum state of energy of the battery,![](data:image/x-wmf;base64...) is the battery installation capacity, ![](data:image/x-wmf;base64...) and ![](data:image/x-wmf;base64...) are charge and discharge power. and are charging and discharging efficiency, and ![](data:image/x-wmf;base64...) is the time interval (1 hour). It is important to note that this model is a theoretical implementation based on the cited methodology and will be parameterized using typical manufacturer specifications for lithium-ion batteries during calculations. A direct experimental validation was not conducted within the scope of this work.

In PFAL-PVBES applications, integrating BES fundamentally reduces grid dependency. However, maximizing performance requires aligning lighting schedules with local spatiotemporal conditions (see Section 2 of the Supplementary Information for more details).

## 2.3 Optimization methodology and workflow

The optimization framework addresses the challenge of sizing PVBES components while considering the temporal dynamics of energy generation and consumption. The three key input variables are: photoperiod start time, PV array area, and battery storage capacity. The goal is to minimize the LCOE for a given payback period (PBP). The LCOE, representing the unit cost of using electricity, is calculated according to Eq. (3):

![](data:image/x-wmf;base64...) (3)

where ![](data:image/x-wmf;base64...) is the investment in the year ![](data:image/x-wmf;base64...), ![](data:image/x-wmf;base64...) is the maintenance and operation cost, ![](data:image/x-wmf;base64...) is the grid electricity cost, ![](data:image/x-wmf;base64...) is the discount rate, and ![](data:image/x-wmf;base64...) is the system lifetime.![](data:image/x-wmf;base64...) is set as the sum of the load profile of the PFAL [51,52].

The PBP is calculated as the ratio of total capital cost to annual savings, as shown in Eq. (4):

![](data:image/x-wmf;base64...) (4)

where ![](data:image/x-wmf;base64...) represents the total capital cost of the system, and ![](data:image/x-wmf;base64...)represents the annual savings compared to grid-only operation.

To assess energy consumption coverage, here we define the Time-based Grid Dependency (TGD) as the percentage of annual hours during which PV electricity generation and BES stored power are insufficient to meet load demand. This metric reflects the temporal grid dependency of the PFAL-PVBES system. A TGD of 100% indicates that the PFAL-PVBES system requires electricity from the grid at each hour, whereas 0% indicates complete energy autonomy of the PFAL-PVBES system. This is expressed in Eq. (5):

![](data:image/x-wmf;base64...) (5)

here, ![](data:image/x-wmf;base64...) equals 1 when grid import occurs and 0 otherwise, 8760 represents the number of hours per year. We acknowledge that this binary-hour metric provides a conservative estimate of system autonomy, as even minimal grid imports during an hour are counted as grid-dependent for the entire hour.

To provide a more comprehensive assessment of energy self-sufficiency, we also calculate an Energy-based Grid Dependency (EGD) metric, which quantifies the fraction of total annual energy demand met by grid imports:

![](data:image/x-wmf;base64...) (6)

where ![](data:image/x-wmf;base64...) is the grid electricity imported at hour ![](data:image/x-wmf;base64...), and ![](data:image/x-wmf;base64...) is the total load demand at hour ![](data:image/x-wmf;base64...). This metric directly quantifies the proportion of annual energy consumption sourced from the grid, complementing the temporal reliability perspective offered by TGD.

The main constraint is the requirement that the annual maintenance costs of the PVBES (discounted) remain below the annual grid savings, thereby ensuring economic sustainability. The optimization employs an enumeration approach that systematically evaluates all possible combinations within the discretized parameter space.

The optimization workflow for the PFAL-PVBES system design is illustrated in levels 3 and 4 of Fig. 1. The process begins by defining technical and economic parameters, and optimization ranges for PV array area and BES capacity. Location-specific meteorological data, encompassing solar irradiance and temperature, are processed to generate PFAL load profiles for each photoperiod start hour (0-23).

System configurations are systematically evaluated by enumerating parameters in a hierarchical order, with the photoperiod start hour as the primary level, followed by PV array area and BES capacity within their defined ranges. The optimal configuration for each photoperiod start hour is identified by minimizing LCOE among feasible setups. Secondary metrics, such as TGD, are calculated to assess system autonomy and verify compliance with design constraints.

For each location, the framework evaluates 10,584 unique PFAL-PVBES configurations, representing all combinations of 441 PVBES configurations and 24 photoperiod options. This methodology enables the systematic evaluation of the complex interrelationships among system sizing, operational scheduling, and economic performance.

In terms of computational requirements for running this workflow, first, EnergyPlus thermal simulation (~1 minute on an 8-core system with 31 GB RAM) generates annual HVAC load profiles of the PFAL, and second, PFAL-PVBES configuration enumeration (~84 minutes for 24 photoperiod schedules × 10,584 PVBES configurations per schedule). The exhaustive enumeration approach guarantees identification of the global optimum and enables comprehensive visualization of the solution space for design guidance, as discussed in the results sections.

## 2.4 Case Study Setup

To reflect a realistic production scenario, the planting area of the validated EnergyPlus model was increased from 9 m2 to 16 m2, corresponding to a typical production container PFAL with two rows and four layers of cultivation racks [15]. To align with our experimental setup, we employed an LED energy density of 152 W·m-2, assuming continuous full-power operation during the production scenario. Coupled with a constant fan speed and the COP of the air-conditioning system detailed in Section 2.1, this configuration yields an estimated daily energy consumption of approximately 85 kWh.

The key input variables for the simulated PFAL-PVBES system are the photoperiod start hour, PV array area, and BES capacity. The key parameters for PFAL-PVBES used throughout the analysis of commercially available components are summarized in Table 1, with specifications sourced from manufacturer datasheets, established literature, or assumptions. Additionally, to focus on the impact of both photoperiod scheduling and climate characteristics, the electricity price is fixed at 0.096 $·kWh-1. Other key economic parameters are detailed in Table 2. To ensure clarity and reproducibility, the core assumptions underlying the PFAL-PVBES framework are summarized in Table 3.

Table 1. Key PFAL-PVBES parameters used for energy consumption coverage simulation

|  |  |  |
| --- | --- | --- |
| Parameter | Value | Source |
| *PFAL Parameters* | | |
| Size | 20-foot container | Yu et al. [42] |
| Photoperiod duration | 16 hours | Yu et al. [42] |
| LED power per planting area | 152 W·m-2 | Yu et al. [42] |
| Planting area | 16 m2 | Assumption |
| Air-conditioning COP | 2.57-3.94 | Section 2.1 |
| *PV Module Parameters* | | |
| Peak power | 640 W | Jinko Solar [47] |
| Module efficiency | 22.9% | Jinko Solar [47] |
| Temperature coefficient | -0.29%·°C-1 | Jinko Solar [47] |
| Module area | 2.8 m2 (4.3 m2·kWp-1) | Jinko Solar [47] |
| *BES Module Parameters* | | |
| Charging/discharging efficiency | 0.91 | Zhao et al. [41] |
| Capacity per unit | 372.7 kWh | CYBD CATL [49] |
| State of Charge limits | 0.1-0.9 | Zhao et al. [41] |
| Maximum charge/discharge rate | 1.0 C | Zhao et al. [41] |

Table 2. Economic parameters used for energy cost reduction simulation

|  |  |  |
| --- | --- | --- |
| Parameter | Value | Source |
| *Grid Costs* | | |
| Grid Price | 0.096 $·kWh-1 | Assumed |
| *PV Module Costs* | | |
| Capital cost | 120 $·kWh-1 | Alibaba [48] |
| Maintenance cost | 8.29 $·kWh-1 annually | Zhao et al. [42] |
| *BES Module Costs* | | |
| Capital cost | 220 $·kWh-1 | Alibaba [49] |
| Maintenance cost | 1.24 $·kWh-1 annually | Zhao et al. [42] |

Table 3. Summary of key assumptions applied in the modeling of the PFAL-PVBES system

|  |  |  |
| --- | --- | --- |
| Category | Assumption | Justification |
| Thermal Loads | Latent heat from plants is excluded from the air-conditioning load calculations. | All sensible and latent heat gains in PFALs can be attributed to the visible fraction of output of the LED. |
| Equipment Operation | The heat dissipation fraction of the LED is adjusted to 1, while fresh air and fan filter units are set to 0.3. | Validated through experimental measurements of the exemplary container, and the adjustment accounts for the latent heat of plants. |
| Lighting & Fans | The LED system operates continuously at full power (152 W·m-2) during the photoperiod, with a constant fan speed. | Represents a standard production scenario for the container PFALs. |
| Air-conditioning Efficiency | A fixed Seasonal COP is applied rather than hourly dynamic values. | Captures the aggregate efficiency of the system across diverse operating conditions. |
| Economic Parameters | The grid electricity price is fixed at 0.096 $·kWh-1. | Isolates the impact of photoperiod scheduling and climate characteristics on the optimization process. |

# 3. Results

Based on the methods presented in the methodology sections, the results sections first present the PFAL loads generation across different cities. Then, we calculate how PVBES and the photoperiod start hour can be configured to achieve energy autonomy for a production container PFAL in various climates. Afterward, the optimization strategy will be used to design an optimal PFAL-PVBES system for each city. Finally, an uncertainty estimation and a sensitivity analysis will be conducted.

## 3.1 PFAL loads generation in distinct climates for specific photoperiod scheduling

This work uses representative cities from five distinct climate zones in China (Shanghai, Harbin, Haikou, Lasa, and Urumqi) to evaluate PFAL-PVBES performance under a 16-hour photoperiod. These locations exhibit variations in key climate parameters affecting both PFAL energy requirements and PV generation potential. Their corresponding climate data are imported from the Open-Meteo API [43] mentioned in Section 2.

As shown in Fig. 3 (a), Lasa receives the highest annually average solar resource (5.88 kWh·m-2·day-1), followed by Haikou (4.72 kWh·m-2·day-1) and Urumqi (4.21 kWh·m-2·day-1). Harbin shows the lowest solar radiation (3.81 kWh·m-2·day-1). Seasonally, solar resource availability is highest in spring and summer, with Lhasa and Urumqi recording the highest solar radiation levels. In contrast, solar radiation is lowest in winter, particularly in Urumqi, where its high latitude (~43.8 N) results in shorter daylight hours, leading to solar radiation levels comparable to Harbin (~2.2 kWh·m-2·day-1 in winter). Furthermore, as shown in Fig. 3(b), the average temperature profiles clearly distinguish these locations (the error bars indicate their standard deviations), with Haikou exhibiting the highest annual mean temperature (~25.5°C) and substantial seasonal stability. In comparison, Harbin (~5.7°C) shows much lower annual temperatures. The methodology described in Section 2 was used to generate energy load profiles for multiple cities. For each city, 24 distinct profiles were created for the year 2024, each corresponding to a unique photoperiod start time. Fig. 3 (c) illustrates the average daily air-conditioning energy consumption derived from these 24 profiles, with error bars representing the standard deviation of the data.

![G:/PVBES_Design/submission/v14/071611043414_0Climates_A_seasonal_radiation.png071611043414_0Climates_A_seasonal_radiation](data:image/png;base64...)

Fig. 3. Climate characteristics and PFAL energy consumption across the five selected cities. (a) Average daily solar radiation (kWh·m-2·day-1) for each city by season. (b) Annual mean temperatures by season with error bars indicating standard deviation. (c) Simulated daily air-conditioning energy consumption if the container PFAL is deployed in each city, with associated uncertainty ranges. (d) Diurnal solar radiation patterns across six distinct periods throughout the day.

As illustrated in Fig. 3 (c), the projected daily air-conditioning energy consumption would be highest in Haikou (~24 kWh) and Shanghai (~21 kWh), reflecting greater cooling demand in warmer climates. Lasa demonstrates the lowest projected air-conditioning requirement (~18 kWh) despite moderate temperatures, likely due to lower temperatures and reduced cooling needs. Additionally, as shown in Fig. 3 (d), all locations exhibit similar temporal patterns with peak radiation occurring between 12:00 and 16:00, but with significant magnitude differences. Lasa shows the highest peak radiation (~700 W·m-2), followed by Haikou and Shanghai (~500 W·m-2). Temporal distribution patterns significantly influence optimal photoperiod scheduling, as they determine when solar energy is most abundant for direct use or battery charging.

## 3.2 Energy autonomy design

To evaluate the configuration range in which the PVBES system can fully satisfy the energy requirements of the production container PFAL, a parametric analysis enumerates the photoperiod start hour from 00:00 to 23:00 in hourly increments. The PV array area, ranging from 0 to 300 m2 in 10 m2 steps, determines the electricity generation capacity of the PVBES system. The battery storage capacity, ranging from 0 to 200 kWh in 5 kWh increments, governs the ability of the PVBES system to store excess energy for later use.

Using the TGD metric defined in Section 2.3, the analysis adopts a conservative reliability threshold, classifying configurations with TGD < 5% as feasible for autonomous operation, accounting for both potential calculation and real-world uncertainties in the enumeration process.

![030614182447_0Coverage_A_feasible_area](data:image/png;base64...)

Fig. 4. Comprehensive coverage analysis of optimized PFAL-PVBES systems across multiple climatic conditions and operational scenarios. (a) Climate-dependent viable system requirements revealing geographic average feasibility hierarchy from Lasa (40 m2 PV, 40 kWh battery) to Harbin (120 m2 PV, 50 kWh battery). (b) Temporal optimization of plant factory energy systems reveals photoperiod-dependent reliability patterns, with early-morning starts and late-night operations achieving superior performance across all climatic zones. (c) Performance topology for Shanghai through systematic design-space exploration, showcasing the average TGD distribution across various PVBES configurations. (d) Shanghai temporal analysis reveals uniform PV requirements to achieve TGD < 5% but variable BES capacity demands, with morning photoperiods requiring 40% less BES capacity than afternoon starts.

As shown in Fig. 4 (a), the feasible configuration space exhibits geographic variation in minimum system requirements, with distinct boundaries defining the operational envelope for possible TGD < 5% in each city. Quantitative analysis reveals a clear feasibility hierarchy: Lasa achieves the minimum requirements of 40 m2 PV and 40 kWh battery, followed by Haikou (50 m2 PV and 45 kWh battery), Shanghai (80 m2 PV and 50 kWh battery), Urumqi (110 m2 PV and 45 kWh battery), and Harbin (120 m2 PV and 50 kWh battery). Notably, although the annual average solar irradiance in Urumqi, Harbin, and Shanghai is comparable, the requirements in Urumqi and Harbin are significantly higher, primarily because their solar resource availability during winter is lower and offsets contributions from other seasons, thereby increasing their overall energy demands.

To identify temporal optimization opportunities, we evaluated photoperiod timing for each PVBES configuration across multiple cities. Fig. 4 (b) shows that early-morning starts yield the lowest TGD. For instance, in Lasa, the average TGD is around 11% during hours 01:00-03:00, compared to 15.01% during hours 17:00-19:00. This trend suggests potential for optimization through strategic timing.

As shown in Fig. 4 (c), upon closer inspection of deploying a production container PFAL in Shanghai, we calculated the mean TGD across all configurations in the high-resolution performance topology, revealing a transition zone between 95 and 300 m2 PV array area where system reliability improves substantially. As shown in Fig. 4(d), the minimum viable system to achieve a TGD < 5% in Shanghai indicates that PV array area requirements remain uniform across different photoperiod start hours (86.5 ± 4.9 m2). In contrast, BES capacity requirements exhibit significant hour-dependent variation (78.5 ± 20.7 kWh). Morning photoperiod starts (02:00-06:00) require substantially lower BES capacity (50-60 kWh) compared to afternoon starts (13:00-19:00), which require 80-90 kWh. The strategic alignment of photoperiod timing with solar peak hours enables up to 40% reduction in battery requirements while maintaining identical PV sizing.

## 3.3 Economic optimization results

The optimization results show that PFAL-PVBES integration achieves highly competitive LCOE values across all studied climate zones. As illustrated in Fig. 5 (a), systems designed for shorter payback periods (3 years) yield LCOE values ranging from approximately 0.034 $·kWh-1 (Lasa) to 0.042 $·kWh-1 (Shanghai), representing a 57-61% reduction compared to the assumed grid electricity price. When extending to longer payback periods (5 years), LCOE further decreases to between 0.032 $·kWh-1 (Lasa) and 0.039 $·kWh-1 (Shanghai), delivering even greater savings of 59-67% relative to grid electricity. Notably, Lasa consistently outperforms all other locations with the lowest LCOE values, attributable to its optimal combination of abundant solar radiation and moderate temperature profile. These conditions simultaneously enhance PV generation efficiency while reducing the cooling energy requirements of the PFAL. The increased energy cost savings for 5-year payback periods could be attributed to the larger sizes of both PV and BES allowed. As illustrated in Fig. 5 (b), the optimal system configurations vary substantially across locations. For the 3-year payback target, PV array sizes range from 80 m2 (Lasa) to 140 m2 (Harbin), with battery capacities between 60 and 100 kWh. For the 5-year target, both components increase in size, with PV arrays ranging from 60 m2 (Lasa) to 150 m2 (Harbin) and battery capacities from 100 to 145 kWh. Still, because larger sizes yield greater energy savings, overall energy costs are lower. While the optimal area for the PV array in Lasa seems to decrease with a longer PBP, this decrease is countered by an increase in BES capacity from 60 kWh to 100 kWh.

![030614051280_0Results_A_lcoe_payback_analysis](data:image/png;base64...)

Fig. 5. Performance of optimized PFAL-PVBES systems across different cities when considering economical aspects. (a) Optimal LCOE achievable for 3 years versus 5 years payback period targets, with Lasa exhibiting the strongest potential of reducing LCOE by around 60 % for a PBP of under 3 years. (b) Optimal PV array sizing and BES capacity requirements for target payback periods. A longer PBP would enable larger PV array areas and BES capacities, resulting in superior LCOE and TGD performance. (c) The optimal start time for the photoperiod in different cities is either 03:00 or 04:00. (d) The average impact of photoperiod timing on economic performance across all the feasible enumerated solutions. Initiating the photoperiod at 03:00-05:00 is more cost-effective than at 15:00-19:00, as the former aligns with the 16-hour photoperiod and peak solar radiation, thereby enabling more direct solar power use.

These results demonstrate the climate-responsive nature of optimal system sizing. Locations with higher solar radiation and more favorable temperature profiles (like Lasa) can achieve comparable economic performance with smaller PV and BES equipment sizes. In contrast, locations with lower or more seasonally variable solar resources (like Harbin) require larger PV arrays to achieve similar performance metrics.

As shown in Fig. 5 (c), the optimal photoperiod start time for each city is either 03:00 or 04:00 (in accordance with the findings in Section 3.4). With a 16-hour photoperiod, an early photoperiod start aligns high LED demand in PFAL with early and peak solar generation (morning through 12:00-16:00), allowing PV output to directly power PFAL loads while excess energy charges the BES. The dark period, when LED demand is absent, coincides with evening hours, reducing electricity needs. This enables a small BES capacity to meet evening demand, minimizing grid dependency and costs. Further supporting this, Fig. 5 (d) shows that photoperiods starting between 03:00 and 05:00 consistently achieve the lowest LCOE and PBP across all evaluated scenarios. Conversely, later start times (15:00-18:00) increase LCOE and PBP by up to 13.0% and 9.6%, respectively, confirming the advantage of early scheduling for cost-effective PFAL operation.

In addition, the energy-based EGD has been calculated for the optimal configurations of each city. EGD typically ranges from 3% to 9% across the five cities, compared to TGD values of approximately 5%. This confirms that during hours of grid dependency, the magnitude of power import is minimal, further demonstrating the near-energy-autonomy capability of optimized PFAL-PVBES systems (see Section 3 in Supplementary Information for more details).

### 3.4 Uncertainty estimation and sensitivity analysis

To ensure robust results, a systematic assessment of overall uncertainty within the simulation framework was conducted. This analysis integrates the inherent error sources from the three core models. Based on rigorous validation results, the PV model (R2=0.992) and the energy consumption model of the PFAL (R2=0.908) were assigned uncertainty ranges of ±3% and ±10%, respectively, with the PFAL model being the primary contributor to the uncertainty of the system. For the BES model, an uncertainty of ±2% was established. The nature of the model justifies this lower uncertainty range: unlike the PV and PFAL models, which depend on stochastic environmental variables, the BES model operates as a deterministic, rule-based energy balancing module governed by fixed efficiency ratings. Furthermore, the core parameters of the model are derived from manufacturer specifications with high certainty, making a smaller error margin both logical and appropriate. To consolidate these independent error sources into a single metric, the standard Root Sum of Squares method for error propagation was employed. By summing the squares of the individual error rates and taking the square root, the composite uncertainty of the system was calculated to be approximately 10.6%. Consequently, this ±11% value is established as the overall uncertainty for all PFAL-PVBES framework outputs in this work.

Beyond the baseline uncertainty assessment, we conducted sensitivity analyses to verify that our core conclusions remain robust under realistic parameter variations. First, to address potential concerns about the Seasonal COP simplification, we compared our baseline approach against an hourly COP model that accounts for temperature-dependent efficiency degradation:

![](data:image/x-wmf;base64...) (7)

where ![](data:image/x-wmf;base64...) represents the COP degradation coefficient (set as 0.025 °C-1 [53]), ![](data:image/x-wmf;base64...) represents the ambient temperature, and ![](data:image/x-wmf;base64...) represents the reference temperature of 25°C. By setting a hypothetical baseline COP of 3.5, the analysis across all five climate zones reveals that the Seasonal COP approach yields conservative estimates for cold climates (e.g., Lasa: -14.5% reduction in air-conditioning energy consumption) and modest increases for hot climates (e.g., Shanghai: +17.2%, Haikou: +13.4%). This finding accentuates consumption disparities across cities, thereby confirming the trends shown in Fig. 3 (c). Furthermore, the economic impact of these variations remains small relative to the overall system optimization benefits ( < 13 $·month-1 per city compared to at least 3000 $ saved in PVBES sizing), confirming that our simplified approach maintains acceptable accuracy without introducing significant bias.

Second, we conducted a comprehensive battery efficiency sensitivity analysis to ensure our conclusions are robust to battery degradation scenarios. We tested five efficiency levels ranging from 80% (severe degradation) to 95% (high performance), with our baseline using 91% based on manufacturer specifications. The results demonstrate that the early-morning photoperiod strategy (start hour 04:00) consistently outperforms the midday strategy (start hour 13:00) across all efficiency scenarios, with LCOE advantages ranging from 46.9% to 57.8%. This confirms that our core finding, the superiority of sizing-scheduling coordination through early-morning scheduling, remains valid even under severe battery degradation conditions. Ultimately, the consistent performance advantages observed across diverse climatic zones, dynamic temperature variations, and varying stages of battery degradation collectively demonstrate the robust nature of the proposed PFAL-PVBES optimization framework under varying operating conditions.

# Discussion

### 4.1 PFAL-PVBES integration strategy

The resulting integration strategy uses photoperiods that start between 03:00 and 05:00, improving performance by up to 13% by matching LED demand with peak solar generation and reducing the need for batteries. Longer payback periods of 5 years enable 84.1-92.8% reductions in grid dependency with larger PVBES setups. This balances initial costs with long-term savings. Based on the results in Section 3.3, a rough estimate for the 16 m² cultivation area of the studied PFAL shows that 2.5-7.5 m2 of PV and 2.5-3.1 kWh of BES are needed per m2 of cultivation area to meet the full annual electricity demand. This depends on location and weather conditions.

The resulting integration strategy leverages the flexible photoperiod characteristic of PFALs through two key findings. First, regarding operational scheduling, photoperiods starting between 03:00 and 05:00 improve system performance by up to 13% through sizing-scheduling coordination. This coordination reduces battery capacity requirements by up to 40% while maintaining identical PV sizing, a strategic advantage that exists because plant growth depends on cumulative light integral rather than specific timing. This time-shiftable load characteristic fundamentally differentiates PFAL-PVBES systems from conventional building microgrids, where loads are temporally fixed. Second, regarding PVBES capacity design, our analysis reveals nonlinear trade-offs between PV and BES capacity. Based on the results in Section 3, a rough estimate for the 16 m2 cultivation area of the studied PFAL shows that 2.5-7.5 m2 of PV and 2.5-3.1 kWh of BES are needed per m2 of cultivation area to meet the full annually electricity demand. Importantly, minimum thresholds exist for both components below which system performance degrades rapidly, regardless of the size of the other components, necessitating simultaneous optimization rather than sequential component selection.

The optimal PVBES configuration varies substantially across climate zones, revealing distinct regional deployment strategies. Locations with high solar radiation paired with moderate-to-cold temperatures (e.g., Lhasa) represent ideal conditions in which abundant solar resources simultaneously maximize PV generation and minimize cooling loads, achieving the lowest LCOE (0.034 $·kWh-1 for a 3-year PBP) with minimal system sizing (40 m2 PV + 40 kWh BES). In contrast, locations with moderate solar resources and pronounced seasonal variations (e.g., Harbin, Urumqi) require substantially larger PV arrays (110-120 m2) to compensate for winter deficits, despite lower annual cooling demands. The economic viability also depends on regional electricity prices: in high-price regions (> 0.10 $·kWh-1), longer payback periods (5 years), enabling 84.1-92.8% grid independence, become economically attractive, while moderate-price regions may favor 3-year configurations that balance capital investment against operational savings.

Current research frequently recommends shifting the PFALs photoperiod to nighttime hours, such as starting at 18:00, to exploit off-peak electricity prices [54,55]. As shown in Fig. 5. (d), when applying this conventional nighttime benchmark to a PFAL-PVBES system, the temporal mismatch between solar generation and lighting demand forces the system to store daytime solar energy in batteries for evening use. This energy storage requirement increases the necessary battery capacity and incurs energy conversion losses, resulting in an average LCOE of approximately 0.085 $·kWh-1. In contrast, advancing the photoperiod start time to the early morning hours, specifically between 03:00 and 05:00, aligns the energy demand of the LED with the daily peak of solar radiation. This active alignment allows the lighting system to use solar power directly, lowering the average LCOE to approximately 0.072 $·kWh-1. Therefore, the active sizing-scheduling coordination demonstrates a clear economic superiority over the conventional nighttime benchmark strategy.

### 4.2 Scalability and limitations of the research

One key practical challenge is that the optimal PV array areas (80 to 150 m2 for a 20-foot container) identified in this work represent the unconstrained techno-economic optimum, which substantially exceeds the footprint of the container (~15 m2), underscoring the critical impact of spatial constraints on system sizing and energy autonomy. If the available PV array area falls below the identified minimum thresholds, simply increasing BES capacity yields diminishing returns, leading to a rapid degradation in TGD outcomes. To address deployment in land-limited environments, two potential strategies emerge.

First, vertical integration strategies, such as using the expansive rooftop spaces of multi-story industrial or commercial buildings, could deliver aggregated generation capacity to support a cluster of container units. Second, agrivoltaic practices, such as deploying elevated ground-mounted PV arrays, may enable dual land use, generating power above while reserving the ground below for PFAL installation.

When transitioning from a single unit to large-scale commercial deployments, PFAL operators can aggregate multiple cultivation modules and centralize the battery energy storage systems to share capital costs. Accordingly, the PFAL-PVBES modeling framework developed here accommodates such scale-ups by adjusting the ranges of the PV array area and combining the thermal loads during optimization. This adaptability enables feasibility assessments under realistic constraints and demonstrates the scalability of the method for real-world deployment. Additionally, while fixed seasonal COP values provided sufficient accuracy for this work (±11% overall uncertainty), future research could incorporate dynamic COP modeling and explore flexible photoperiod duration based on cumulative daily light integral targets to reveal additional optimization opportunities.

Because this work relies on simulated thermal loads and simplified techno-economic models with fixed parameters, factors such as long-term degradation of PV modules, capacity fade of BES, and dynamic variations in electricity pricing are not captured. Translating these idealized models into real-world implementations of PFALs will inevitably introduce physical installation constraints, microgrid integration complexities, and nonlinear scaling effects on the efficiency of cooling equipment. Therefore, future research must validate these simulation-based findings through long-term pilot demonstrations to address operational uncertainties and provide empirical confidence intervals for investment decisions.

### 4.3 Open-source release

To support the advancement of PFAL-PVBES research and enable practitioners to tailor designs to specific conditions, we released the simulation and optimization framework as OpenCROPS (Climate-Responsive Optimizer for Plant System) [56]. This open-source platform equips researchers and practitioners with tools to model PFAL energy consumption, simulate PVBES performance, and optimize designs for specific climatic, economic, and spatial constraints. By providing transparent, reproducible methods, OpenCROPS invites the research community to build upon these models and strategies, enabling exploration of new PFAL-PVBES configurations and supporting the global expansion of sustainable, energy-efficient food production systems.

# 5. Conclusion

This work addresses the critical barrier of high energy costs in PFALs by proposing a sizing-scheduling coordination strategy for PFAL-PVBES integration. Unlike previous research that generally adopted passive PFAL-PVBES integration strategies based on fixed load profiles, this work successfully shifts the design paradigm toward active load coordination, exploiting the unique temporal flexibility of artificial lighting schedules in PFALs.

First, our analysis of a standard 20-foot container PFAL (16 m2 cultivation area) established the specific PFAL-PVBES sizing benchmarks required to achieve energy autonomy. Crucially, this analysis is supported by one full year of operational data from a functioning PFAL, ensuring that the identified benchmarks reflect real-world thermal and electrical dynamics. As a result, we found that achieving a TGD of less than 5% requires distinct configurations depending on the climate: ranging from a minimum of 40 m2 PV and 40 kWh battery capacity in favorable climates like Lasa, to 120 m2 PV and 50 kWh battery capacity in resource-constrained regions like Harbin. Our climatic assessment confirms that locations combining high solar resources with moderate-to-cold temperatures are the most favorable for PVBES deployment, as they simultaneously maximize PV generation and minimize cooling loads.

Second, our sizing-scheduling coordination strategy demonstrates another key outcome: photoperiod timing in PFAL is as critical as PVBES component sizing. As a practical implication, shifting the photoperiod start time to the early morning hours (03:00-05:00) actively aligns the high-energy demand of LED lighting with the daily solar radiation peak. This active coordination enables direct solar self-consumption, significantly reducing the required battery capacity by up to 40% compared to conventional schedules while maintaining identical energy autonomy.

Furthermore, the economic optimization results reveal that these strategies make PFAL-PVBES systems highly cost-competitive. The optimized configurations achieved an LCOE between 0.034 and 0.042 $·kWh-1, representing a cost reduction of 57-67% compared to a fixed grid electricity prices. Moreover, allowing a longer payback period (5 years) enables larger system sizes that can reduce TGD by up to 92.8%, paving the way for energy autonomy in PFALs.

Finally, we identified that the optimal PV array sizes (80-150 m2) often exceed the physical footprint of the container itself, suggesting that future deployments should prioritize vertical integration on building rooftops or agrivoltaic setups to overcome spatial constraints. To facilitate future improvement and applications, we have released our simulation findings through the open-source OpenCROPS framework, inviting researchers and practitioners to tailor these models to their local climatic and spatial conditions to further advance sustainable urban agriculture.

# Acknowledgments

This research is supported by the Shanghai Agriculture Applied Technology Development Program [Grant No.2023-02-08-00-12-F04621], National Nature Science Foundation of China [Grant No. W2542029], and the Science and Technology Development Fund (Innovation Fund of Agricultural Project) of Shanghai Pudong [Grant No. PKJ2024-N08].

# References

[1]Béné C. Resilience of local food systems and links to food security—a review of some important concepts in the context of COVID-19 and other shocks. Food Secur 2020;12:805-22. <https://doi.org/10.1007/s12571-020-01076-1>

[2]Vogel E, et al. The effects of climate extremes on global agricultural yields. Environ Res Lett 2019;14:054010. <https://doi.org/10.1088/1748-9326/ab154b>

[3]Benke K, Tomkins B. Future food-production systems: vertical farming and controlled-environment agriculture. Sustain Sci Pract Policy 2017;13:13-26. <https://doi.org/10.1080/15487733.2017.1394054>

[4]Kozai T, Niu G, Takagaki M (Eds.). Plant Factory: An Indoor Vertical Farming System for Efficient Quality Food Production. Academic Press; 2019.

[5]Yokoyama R. Energy Consumption and Heat Sources in Plant Factories. In: Plant Factory Using Artificial Light. Elsevier; 2019: 177-184.

[6]Graamans L, Tenpierik M, van den Dobbelsteen A, Stanghellini C. Plant factories: Reducing energy demand at high internal heat loads through façade design. Appl Energy 2020;262:114544. <https://doi.org/10.1016/j.apenergy.2020.114544>

[7]Weidner T, Yang A, Hamm MW. Energy optimization of plant factories and greenhouses for different climatic conditions. Energy Convers Manag 2021;243:114336. <https://doi.org/10.1016/j.enconman.2021.114336>

[8]Hu G, You F. AI-enabled cyber-physical-biological systems for smart energy management and sustainable food production in a plant factory. Applied Energy 2024;356:122334. <https://doi.org/10.1016/j.apenergy.2023.122334>.

[9]Graamans L, Baeza E, van den Dobbelsteen A, Tsafaras I, Stanghellini C. Plant factories versus greenhouses: comparison of resource use efficiency. Agric Syst 2018;160:31-43. <https://doi.org/10.1016/j.agsy.2017.11.003>.

[10]Olvera-Gonzalez E, Escalante-Garcia N, Myers D, Ampim P, Obeng E, Alaniz-Lumbreras D, et al. Pulsed LED-Lighting as an Alternative Energy Savings Technique for Vertical Farms and Plant Factories. Energies 2021;14:1603. <https://doi.org/10.3390/en14061603>.

[11]Xu D, Ahmed HA, Tong Y, Yang Q, Van Willigenburg LG. Optimal control as a tool to investigate the profitability of a Chinese plant factory - lettuce production system. Biosystems Engineering 2021;208:319-32. <https://doi.org/10.1016/j.biosystemseng.2021.05.014>

[12]Cai W, Bu K, Zha L, Zhang J, Lai D. Energy Consumption of PFAL with Artificial Light: Challenges and Opportunities. Renew Sustain Energy Rev 2023; <https://doi.org/10.1016/j.rser.2024.115235>

[13]Bu K, Yu Z, Lai D, Bao H. Energy-saving effect assessment of various factors in container plant factories: A data-driven random forest approach. Clean Energy Syst 2024;8:100122. <https://doi.org/10.1016/j.cles.2024.100122>

[14]Arcasi A, Mauro AW, Napoli G, Tariello F, Vanoli GP. Energy and cost analysis for a crop production in a vertical farm. Appl Therm Eng 2024;239:122129. <https://doi.org/10.1016/j.applthermaleng.2023.122129>

[15]Song R, Liu D, Pan Y, Cheng Y, Meng C. Container farms: Energy modeling considering crop growth and energy-saving potential in different climates. J Clean Prod 2023;420:138353. <https://doi.org/10.1016/j.jclepro.2023.138353>

[16]Cai W, Li S, Zha L, He J, Zhang J, Bao H. Significantly enhanced energy efficiency through reflective materials integration in plant factories with artificial light. Applied Energy 2025;377:124587. <https://doi.org/10.1016/j.apenergy.2024.124587>.

[17]Trommsdorff Max, Kang Jinsuk, Reise Christian, Schindele Stephan, Bopp Georg, Ehmann Andrea, et al. Combining food and energy production: Design of an agrivoltaic system applied in arable and vegetable farming in Germany. Renew. Sustain. Energy Rev. 2021;140:110694. https://doi.org/10.1016/j. rser.2020.110694.

[18]Ezzaeri K, Fatnassi H, Wifaya A, Bazgaou A, Gourdo L, Aharoune A, et al. Effects of roof-mounted flexible photovoltaic panels on solar radiation and tomato yield in a Canarian greenhouse. Acta Hortic. 2020;(1296):87-92. https://doi.org/10.17660/ ActaHortic.2020.1296.12.

[19]Cossu Marco, Murgia Lelia, Ledda Luigi, Deligios Paola A, Sirigu Antonella, Chessa Francesco, et al. Solar radiation distribution inside a greenhouse with south-oriented photovoltaic roofs and effects on crop productivity. Appl. Energy. 2014;133:89-100. https://doi.org/10.1016/j.apenergy.2014.07.070.

[20]Kadowaki Masayuki, Yano Akira, Ishizu Fumito, Tanaka Toshihiko, Noda Shuji. Effects of greenhouse photovoltaic array shading on Welsh onion growth. Biosyst. Eng. 2012;111(3):290-7. https://doi.org/10.1016/j.biosystemseng.2011.12.006.

[21]Alramlawi M, Li P. Design Optimization of a Residential PV-Battery Microgrid With a Detailed Battery Lifetime Estimation Model. IEEE Trans Ind Appl 2020;56:2020-30. <https://doi.org/10.1109/TIA.2020.2965894>

[22]El Mezdi K, El Magri A, Watil A, El Myasse I, Bahatti L, Lajouad R, et al. Nonlinear control design and stability analysis of a hybrid grid-connected photovoltaic-Battery energy storage system with an ANN-MPPT method. J Energy Storage 2023;72:108747. <https://doi.org/10.1016/j.est.2023.108747>

[23]El Sayed A, Ahmed EEE, Poyrazoglu G. Optimal Planning and Allocation of DER in Radial Distribution Networks Using IPSO. 2024 IEEE 8th Energy Conference (ENERGYCON), Doha, Qatar: IEEE; 2024. p. 1-6. <https://doi.org/10.1109/ENERGYCON58629.2024.10488786>

[24]Liang Y, Li P, Su W, Li W, Xu W. Development of green data center by configuring photovoltaic power generation and compressed air energy storage systems. Energy 2024;292:130516. <https://doi.org/10.1016/j.energy.2024.130516>

[25]Yano A, Cossu M. Energy sustainable greenhouse crop cultivation using photovoltaic technologies. Renewable and Sustainable Energy Reviews 2019;109:116-37. <https://doi.org/10.1016/j.rser.2019.04.026>.

[26]Fernández EF, Villar-Fernández A, Montes-Romero J, Ruiz-Torres L, Rodrigo PM, Manzaneda AJ, et al. Global energy assessment of the potential of photovoltaics for greenhouse farming. Applied Energy 2022;309:118474. <https://doi.org/10.1016/j.apenergy.2021.118474>.

[27]Li L, Li X, Chong C, Wang C-H, Wang X, A decision support framework for the design and operation of sustainable urban farming systems, Journal of Cleaner Production (2020), doi: https://doi.org/10.1016/j.jclepro.2020.121928.

[28]Fu X, Zhou Y. Collaborative optimization of PV greenhouses and clean energy systems in rural areas. IEEE Trans Sustain Energy 2023;14:642-56. <https://doi.org/10.1109/TSTE.2022.3223684>

[29]Petrakis T, Ioannou P, Kitsiou F, Kavga A, Grammatikopoulos G, Karamanos N. Growth and Physiological Characteristics of Strawberry Plants Cultivated under Greenhouse-Integrated Semi-Transparent Photovoltaics. Plants 2024;13:768. <https://doi.org/10.3390/plants13060768>

[30]Hu Guoqing, You Fengqi. Assessment of photovoltaic-based controlled environment agriculture as a viable solution for enhancing energy efficiency, profitability, and environmental sustainability in major cities. Chemical Engineering Transactions 2024;114:373-8. <https://doi.org/10.3303/CET24114063>.

[31]Naghibi Z, Ekhtiari S, Carriveau R, Ting DS. Hybrid solar thermal/photovoltaic-battery energy storage system in a commercial greenhouse: performance and economic analysis. Energy Storage 2021;3:e215. <https://doi.org/10.1002/est2.215>

[32]Marucci A, Zambon I, Colantoni A, Monarca D. A combination of agricultural and energy purposes: Evaluation of a prototype of photovoltaic greenhouse tunnel. Renew Sust Energ Rev 2018;82:1178-86. <https://doi.org/10.1016/j.rser.2017.09.029>

[33]Li C, Wang H, Miao H, Ye B. The economic and social performance of integrated photovoltaic and agricultural greenhouses systems: Case study in China. Appl Energy 2017;190:204-12. <https://doi.org/10.1016/j.apenergy.2016.12.121>

[34]Cho J, Park SM, Park AR, Lee OC, Nam G, Ra I-H. Application of Photovoltaic Systems for Agriculture: A Study on the Relationship between Power Generation and Farming for the Improvement of Photovoltaic Applications in Agriculture. Energies 2020;13:4815. <https://doi.org/10.3390/en13184815>.

[35]Kozai T, Niu G. Challenges for the next-generation PFALs. Plant Factory, Elsevier; 2020, p. 463-9. <https://doi.org/10.1016/B978-0-12-816691-8.00032-7>

[36]Chen H, Dong X, Lei J, Zhang N, Wang Q, Shi Z, et al. Life cycle assessment of carbon capture by an intelligent vertical plant factory within an industrial park. Sustainability 2024;16:697. <https://doi.org/10.3390/su16020697>

[37]Kikuchi Y, Kanematsu Y, Yoshikawa N, Okubo T, Takagaki M. Environmental and resource use analysis of plant factories with energy technology options: A case study in Japan. J. Cleaner. Prod. 2018;186:703-717. <https://doi.org/10.1016/j.jclepro.2018.03.110>

[38]Drottberger A, Zhang Y, Yong JWH, Dubois M-C. Urban farming with rooftop greenhouses: A systematic literature review. Renew Sust Energ Rev 2023;188:113884. <https://doi.org/10.1016/j.rser.2023.113884>

[39]Uraisami K. Renewable energy makes plant factory "smart". In Smart Plant Factory, T. Kozai, ed. (Singapore: Springer), 2018, p. 119123. [https://doi.org/10.1007/978-981-13-1065-2\_7](https://doi.org/10.1007/978-981-13-1065-2%E5%AC%B27)

[40]Jiang J-A, Su Y-L, Shieh J-C, Kuo K-C, Lin T-S, Lin T-T, et al. On the application of a new hybrid maximum power point tracking (MPPT) based photovoltaic system to the closed plant factory. Applied Energy 2014;124:309-24. <https://doi.org/10.1016/j.apenergy.2014.03.017>.

[41]Zhao Y-B, Dong X-J, Shen J-N, He Y-J. Simultaneous sizing and scheduling optimization for PV-wind-battery hybrid systems with a modified battery lifetime model: A high-resolution analysis in China. Applied Energy 2024;360:122812. <https://doi.org/10.1016/j.apenergy.2024.122812>.

[42]Yu Z, Bu K, Liu Y, Wang A, Yuan W, Xue J, et al. Energy examination and optimization workflow for container farms: A case study in Shanghai, China. Applied Energy 2024;374:124038. <https://doi.org/10.1016/j.apenergy.2024.124038>.

[43]Open-Meteo. Open-Meteo API. 2023. <https://open-meteo.com/en/docs/historical-weather-api>

[44]Hersbach H, et al. The ERA5 global reanalysis. Q J R Meteorol Soc 2020;146(730):1999-2049. <https://doi.org/10.1002/qj.3803>

[45]Jerez S, et al. The impact of climate change on photovoltaic power generation in Europe. Nature Communications 2015;6:10014. <https://doi.org/10.1038/ncomms10014>

[46]Gutiérrez-Martín F, Díaz-López JA, Caravaca A, Dos Santos-García AJ. Modeling and simulation of integrated solar PV - hydrogen systems. International Journal of Hydrogen Energy 2024;52:995-1006. <https://doi.org/10.1016/j.ijhydene.2023.05.179>

[47]Jinko Solar. Tiger Neo N-type Technology Technical Specifications. Jinko Solar Inc., Technical Datasheet, 2023.

[48]Alibaba. Jinko Solar Tiger Neo N-Type 640W PV Modules. Alibaba.com Marketplace Listing, [https://www.alibaba.com/product-detail/Jinko-Tiger-Neo-640w-panel-solar\_1600677412104.html](https://www.alibaba.com/product-detail/Jinko-Tiger-Neo-640w-panel-solar%E5%AC%B21600677412104.html), Accessed January 2024.

[49]Alibaba. CBYD CATL LiFePO4 Battery Energy Storage System 372.7kWh. Alibaba.com Marketplace Listing, [https://www.alibaba.com/product-detail/CATL-Battery-CBYD-100Ah-280Ah-LiFePO4\_1600941690182.html](https://www.alibaba.com/product-detail/CATL-Battery-CBYD-100Ah-280Ah-LiFePO4%E5%AC%B21600941690182.html), Accessed January 2024.

[50]CBYD c. CATL Commercial & Industrial Battery System Product Specification. CBYD Energy Technology Co., Ltd., Technical Datasheet, 2023.

[51]Mundada AS, Shah KK, Pearce JM. Levelized cost of electricity for solar photovoltaic, battery and cogeneration hybrid systems. Renewable and Sustainable Energy Reviews 2016;57:692-703. <https://doi.org/10.1016/j.rser.2015.12.084>.

[52]Colmenar-Santos A, De Palacio C, Enríquez-García L, López-Rey Á. A methodology for assessing islanding of microgrids: Between utility dependence and off-grid systems. Energies 2015;8:4436-54. <https://doi.org/10.3390/en8054436>.

[53]Domanski, P. A., Henderson, H. I., & Payne, W. V. (2014). Sensitivity Analysis of Installation Faults on Heat Pump Performance. National Institute of Standards and Technology. [https://doi.org/10.6028/nist.tn.1848](https://www.google.com/search?q=https://doi.org/10.6028/nist.tn.1848" \t "_blank)

[54]Zhang Y, Kacira M. Enhancing resource use efficiency in plant factory. Acta Hortic 2020;1296:15-22. [https://doi.org/10.17660/ActaHortic.2020.1296.2](https://www.google.com/search?q=https://doi.org/10.17660/ActaHortic.2020.1296.2" \t "_blank)

[55]Zhen S, Bugbee B. Continuous lighting can improve yield and reduce energy costs while increasing or maintaining nutritional contents of microgreens. Front Plant Sci 2022;13:836696. [https://doi.org/10.3389/fpls.2022.836696](https://www.google.com/search?q=https://doi.org/10.3389/fpls.2022.836696" \t "_blank)

[56]OpenCROPS. Climate-Responsive Optimizer for Plant System. GitHub repository 2024. [https://github.com/ThomasXIONG151215/OpenCROPS](https://github.com/pfal-energy/OpenCROPS)

# Supplementary Information

**Photovoltaic-battery integration strategy in plant factories with artificial lighting**

***Thomas Xiong1, Wenyi Cai1, Yue Hu2, Mengxuan Song3, TingTing Qian4\*, Hua Bao1\****

1Global Institute of Future Technology, Shanghai Jiao Tong University, Shanghai 200240, China

2CTG Wuhan Science and Technology Innovation Park, China Three Gorges Corporation, Wuhan 430010, China

3School of Energy and Materials, Shanghai Polytechnic University, Shanghai 201209, China

4Agricultural Information Institute of Science and Technology, Shanghai Academy of Agricultural Sciences, Shanghai 201403, China

# 1. PV modeling parameters

The module temperature is calculated from ambient temperature and solar irradiance using the nominal operating cell temperature approach [46]. The light-generated current is adjusted for both irradiance and temperature effects:

![](data:image/x-wmf;base64...) (S1)

where ![](data:image/x-wmf;base64...) is the short-circuit current at standard test conditions,is the solar irradiance, ![](data:image/x-wmf;base64...) is the irradiance at standard test conditions, ![](data:image/x-wmf;base64...) is the temperature coefficient for short-circuit current, ![](data:image/x-wmf;base64...) is the module temperature, ![](data:image/x-wmf;base64...) is the reference temperature.

Similarly, the open-circuit voltage is adjusted using:

![](data:image/x-wmf;base64...) (S2)

where ![](data:image/x-wmf;base64...) is the open-circuit voltage at standard test conditions, ![](data:image/x-wmf;base64...) is the temperature coefficient for open-circuit voltage, and the other parameters are as defined above. The maximum power point of the PV modules is determined through an iterative quadratic approximation method [46]. This approach involves formulating and solving a quadratic equation in terms of the current at the maximum power point, then calculating the corresponding voltage and maximum power. The iterative process continues until convergence is achieved, typically within 3 to 5 iterations. The model is validated against selected manufacturer specifications across different irradiance levels (200-1000 W·m-2) and temperatures, with agreement observed between simulated and rated maximum power outputs (see Fig. S1 (c)).

![](data:image/png;base64...)

Fig. S1. Validation of the load profile generation model of the exemplary PFAL and the power generation model of the PV modules. Models performance are evaluated using the coefficient of determination ![](data:image/x-wmf;base64...), the coefficient of variation of the root mean square error ![](data:image/x-wmf;base64...), and the normalized mean square error ![](data:image/x-wmf;base64...). (a) Two-week comparison (August 2023) of measured versus predicted air-conditioning electricity usage in the exemplary PFAL, the results demonstrate strong model reliability (![](data:image/x-wmf;base64...), ![](data:image/x-wmf;base64...), ![](data:image/x-wmf;base64...)). (b) Influence of envelope thermal conductivity and thickness on annual air-conditioning energy demand. Increasing envelope thickness and reducing thermal conductivity mitigate the impact of outdoor weather fluctuations, thereby reducing reliance on air conditioning and lowering energy consumption in PFALs. (c) Comparison of simulated PV output with manufacturer specifications across varying irradiance levels shows high accuracy (![](data:image/x-wmf;base64...), ![](data:image/x-wmf;base64...), ![](data:image/x-wmf;base64...)). (d) Combined effects of irradiance and ambient temperature on PV power output. When the ambient temperature increases, PV output decreases, while an increase in solar irradiance increases it.

# 2. PFAL-PVBES coupling mechanism demonstration

To illustrate the practical operation of PFAL-PVBES systems, a demonstration is proposed to showcase component interactions. For this demonstration, this work extracts the load profile from the exemplary PFAL (with 9 m2 of planting area and 16 hours of photoperiod) during May 1-3, 2024. Figs. S2 (a)-(d) illustrate four PFAL-PVBES configurations: PV-only systems with 30 m2 arrays initiating photoperiods at 04:00 (PV04) or 20:00 (PV20), and battery-integrated variants (PVB04/PVB20) combining 30 m2 PV arrays with 10 kWh storage capacity. Quantitatively, the configurations exhibit clear performance differences in PV utilization and grid reliance. For demonstrative purposes, we defined PV utilization as the fraction of total PV-generated power consumed by the system. We also defined grid reliance to measure the portion of total load demand met by either direct PV power or PV energy discharged from BES. The PV04 configuration achieves 35.0% PV utilization with 48.1% grid reliance, whereas PVB04 improves utilization to 43.7% while reducing grid reliance to 35.1%. In contrast, PV20 shows lower utilization (22.7%) and higher grid dependence (66.2%), while PVB20 achieves 32.0% utilization with 52.3% grid reliance.

Battery integration consistently enhances system performance across both temporal scenarios. For the 04:00 photoperiod start, battery integration increases PV utilization by 8.7 % while reducing grid dependency by 13.0%. Similarly, for the 20:00 start, battery integration yields a 9.3% improvement in utilization and a 13.9% reduction in grid dependency. Notably, in this demonstration, the 04:00 start time outperforms the 20:00 start time, underscoring the importance of context-specific analysis in system design.

![](data:image/png;base64...)

Fig. S2. Performance mechanism demonstration of PVBES. The orange and blue areas in each plot represent daytime and nighttime, respectively. (a) PV-only with 04:00 photoperiod start (PV04), (b) PV with battery and 04:00 photoperiod start (PVB04), (c) PV-only with 20:00 photoperiod start (PV20), and (d) PV with battery and 20:00 photoperiod start (PVB20), demonstrating partial impacts of battery integration and photoperiod scheduling on system performance.

From a temporal perspective, distinct operational dynamics emerge across configurations. In the PV04 scenario (Fig. S2 (a)), grid electricity imports are required during the early morning hours, when PV generation is minimal. As daylight intensifies, PV generation becomes sufficient to meet the energy demands of the PFALs during most of the light period. However, during nighttime hours, the system must revert to grid dependency because PV generation is absent. In contrast, the PVB04 configuration (Fig. S2 (b)) demonstrates a more efficient energy utilization pattern, where excess midday PV generation charges the battery (green), which subsequently discharges (red) during periods of low or zero generation. The 20:00 start photoperiod configurations present alternative operational patterns. The PFAL operates at peak power during evening hours when PV generation is absent. As shown in Fig. S2(c) and (d), this temporal misalignment results in increased grid dependency.

Three principal observations emerge from this demonstration: First, BES integration consistently reduces grid dependency across both photoperiod schedules, demonstrating its fundamental value for PFAL-PVBES applications. Second, the significant performance differential between the 04:00 and 20:00 photoperiods in Shanghai during early May underscores the critical importance of location-specific and temporally optimized scheduling. Third, this demonstration reveals substantial room for improvement in system configuration, particularly given economic factors not addressed in this preliminary analysis.

# 3. Grid dependency metrics comparison

To provide a comprehensive assessment of the PFAL-PVBES system autonomy, we calculated both TGD and EGD metrics: The temporal metric provides a conservative reliability assessment, while the energy metric quantifies the actual magnitude of grid energy dependence.

Table S1. Grid dependency metrics for optimal PVBES configurations across five cities.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| City | Photoperiod Start | PV (m2) | BES (kWh) | TGD (%) | EGD (%) |
| Lasa | 01:00 | 40 | 40 | 4.8 | **3.15** |
| Haikou | 21:00 | 50 | 45 | 4.9 | **5.60** |
| Urumqi | 23:00 | 110 | 45 | 5.0 | **7.90** |
| Harbin | 21:00 | 120 | 50 | 5.1 | **8.40** |
| Shanghai | 20:00 | 80 | 50 | 5.2 | **9.05** |

From Table S1, it can be validated that with an EGD of only 3.15%, Lasa demonstrates the highest level of energy autonomy among all cities. The advantage in Lasa stems from its abundant solar resources and low cooling demand, creating ideal conditions for PFAL-PVBES integration.

On the other hand, cities with high solar resources (Lasa, Haikou) show EGD values close to or lower than their TGD values, indicating that grid imports are distributed relatively evenly across dependency hours. In contrast, cities with more variable solar resources (Shanghai, Harbin) exhibit EGD values significantly higher than their temporal counterparts, suggesting that grid imports are concentrated in specific hours with large deficits (e.g., winter evenings).

Finally, for most cities, EGD values below 10% indicate that optimized PFAL-PVBES systems can achieve near-complete energy autonomy, with grid imports serving primarily as backup during rare deficit periods rather than as a primary energy source.