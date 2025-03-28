---
layout: page
title: SERG Publications
description: Publications by the Software Engineering Research Group at TU Delft.
---


The TU Delft institutional repository maintains a list of [all SERG publications](https://research.tudelft.nl/en/organisations/software-engineering/publications/). 
Clicking on a title link in a publication in the list below will lead you to that publication's page in our insitutional repository, where (for papers since 2016) you usually can find an author-prepared accepted version as well ([green open access](https://avandeursen.com/2016/11/06/green-open-access-faq/)).
The [SERG Technical Reports](/tr) series contains open access preprints of our publications, as well as longer versions including detailed appendices. The series was started in 2006.
The [SERG Dissertation Series](../phd) includes the dissertations written by SERG PhD students since 2006.

### Publication List

<div id="publicationlist"></div>

<script language="javascript">

  var purexml_SERG = "https://purexml-open.ewi.tudelft.nl/direct/tu/group/d40bac4b-3dd0-4427-aa5f-9331cae5d02e";
  var page_nr = location.search;

  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("publicationlist").innerHTML = this.responseText;
    }
  };
  xhttp.open("GET", purexml_SERG + page_nr, true);
  xhttp.send();
</script>
