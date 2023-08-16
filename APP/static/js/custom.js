var flag = false;
if (!flag) {
    const Addformset = document.getElementById("Add_formset")
    const TotalNewForms = document.getElementById("id_Product-TOTAL_FORMS")
    Addformset.addEventListener("click", (event) => {
        const CurrentForms = document.getElementsByClassName("formset")
        let CurrentFormsCount = CurrentForms.length
        const formsetList = document.getElementById("formset-list")
        const clonemyformset = document.getElementById("myformset").cloneNode(true)
        clonemyformset.setAttribute("class", "formset")
        clonemyformset.setAttribute("id", `form-${CurrentFormsCount}`)
        const regex = new RegExp("__prefix__", "g")
        clonemyformset.innerHTML = clonemyformset.innerHTML.replace(regex, CurrentFormsCount)
        TotalNewForms.setAttribute("value", CurrentFormsCount + 1)
        formsetList.append(clonemyformset)
    })
    flag = true;
}