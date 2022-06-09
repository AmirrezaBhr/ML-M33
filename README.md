# ML-M33
"Using classical Machine Learning algorithms and neural networks to detect AGB variables stars in M33 galaxy"

The main aim of this project is to categorize stars. We are searching for variable stars that most
of them are AGB(asymptotic giant branch, The asymptotic giant branch (AGB) is a region of the
Hertzsprung–Russell diagram populated by evolved cool luminous stars. This is a period of
stellar evolution undertaken by all low- to intermediate-mass stars (0.6–10 solar masses) late in
their lives.) stars.
\n
Detecting AGB variable stars is a powerful tool in reconstructing the star formation history of a
galaxy as these stars are in the final stages of their evolution and hence their luminosity is more
directly related to their birth mass than less-evolved AGB stars that still undergo significant
evolution in luminosity. They are also one of the most important sources of produced dust in the
universe, therefore, they help star formation. Detected variable AGB stars through “Machine
learning” can help follow-up observations which are searching for the origin of dust sources in
the universe.
\n
Data set was obtained in J, K and H band with UIST, UFTI, WFCAM instruments(UKIRT data),
but the most extensive data set was obtained in the K band with the UIST instrument for the
central 4 × 4 arcmin^2 (1 kpc^2) – this contains the nuclear star cluster and inner disc. These
data, taken during the period 2003–2007, were complemented by J- and H-band images.
Photometry was obtained for 18 398 stars in this region.
There are several ways to identify variable AGB stars, We used equations in Stetson 1993 and
1996 papers to find variable stars among all observations. As it is mentioned observations were
in K or J filters depending on each star. Based on data gathered we designed an algorithm using
Python to find variable stars and pick them for next steps in this project. Finally, 800 stars were
found to be variable. We want to use this data set to let the machine learn from it how to identify
variable AGB stars by testing various ML algorithms on it, then we are going to find the
optimum algorithm for this kind of data set.
Additionally, we have a new data set of the M33 galaxy gathered by the GAIA telescope which
has never been modified precisely in any other papers before. We aim to resolve the central part
of the M33 galaxy by cross correlating:(A method in which we can modify our observation data
and omit irrelevant stars based on their coordinates.) UKIRT data with GAIA catalogues.
In the next step, we are going to run the optimum ML algorithm in this new data set to identify
AGB variable stars.
In recapitulation, we have an optimized machine learning algorithm for the same observational
projects in future which not only does have the ability to help us but also has a variety of
applications in others’ astronomical projects.
After accomplishing all goals that we set above, we will run the
optimized machine learning algorithm to identify variable stars of another spiral galaxy in the
vicinity of ours.
