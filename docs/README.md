# judilibre_client.DefaultApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**decision**](DefaultApi.md#decision) | **GET** /decision | Permet de récupérer le contenu intégral d&#39;une décision.
[**export**](DefaultApi.md#export) | **GET** /export | Permet d&#39;effectuer un export par lot de décisions de justice.
[**healthcheck**](DefaultApi.md#healthcheck) | **GET** /healthcheck | Permet de récupérer l&#39;état de disponibilité du service.
[**search**](DefaultApi.md#search) | **GET** /search | Permet d&#39;effectuer une recherche dans les données ouvertes des décisions de justice.
[**stats**](DefaultApi.md#stats) | **GET** /stats | Permet de récupérer des statistiques sur le contenu de la base JUDILIBRE.
[**taxonomy**](DefaultApi.md#taxonomy) | **GET** /taxonomy | Permet de récupérer les listes des termes employés par le processus de recherche.


# **decision**
> decision(id, resolve_references=resolve_references, query=query, operator=operator)

Permet de récupérer le contenu intégral d'une décision.

Connaissant l'identifiant unique d'une décision, le point d'entrée `GET /decision` permet d'en récupérer le contenu intégral (structuré, mais sans mise en forme), à savoir :  * L'identifiant de sa juridiction ; * L'identifiant de sa chambre ; * Sa formation ; * Son numéro de pourvoi ; * Son ECLI (« European Case Law Identifier » : identifiant européen de la jurisprudence) ; * Son code NAC ; * Son niveau de publication ; * Son numéro de publication au bulletin ; * Sa solution ; * Sa date ; * Son texte intégral ; * Les délimitations des principales zones d'intérêt de son texte intégral (introduction, exposé du litige, moyens, motivations, dispositif et moyens annexés) ; * Ses éléments de titrage ; * Son sommaire ; * Ses documents associés (communiqué, note explicative, traduction, rapport, avis de l'avocat général, etc.) ; * Les textes appliqués ; * Les rapprochements de jurisprudence.  Certaines des informations ne sont retournées que sous forme de clé ou d'identifiant numérique (juridiction, chambre, niveau de publication, etc.). Il convient dès lors d'utiliser le point d'entrée `GET /taxonomy` pour en récupérer l'intitulé complet, ou d'effectuer la requête en utilisant le paramètre `resolve_references=true`.

### Example
```python
from __future__ import print_function
import time
import judilibre_client
from judilibre_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = judilibre_client.DefaultApi()
id = NULL # object | Identifiant de la décision à récupérer.
resolve_references = NULL # object | Lorsque ce paramètre vaut `true`, le résultat de la requête contiendra, pour chaque information retournée par défaut sous forme de clé, l'intitulé complet de celle-ci (vaut `false` par défaut). (optional)
query = NULL # object | Chaîne de caractères correspondant à la recherche. Ce paramètre est utilisé pour surligner en retour, dans le texte intégral de la décision, les termes correspondant avec la recherche initiale (ces termes étant délimitées par des balises `<em>`). (optional)
operator = NULL # object | Opérateur logique reliant les multiples termes que le paramètre `query` peut contenir (`or` par défaut, `and` ou `exact` – dans ce dernier cas le moteur recherchera exactement le contenu du paramètre `query`). (optional)

try:
    # Permet de récupérer le contenu intégral d'une décision.
    api_instance.decision(id, resolve_references=resolve_references, query=query, operator=operator)
except ApiException as e:
    print("Exception when calling DefaultApi->decision: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| Identifiant de la décision à récupérer. | 
 **resolve_references** | [**object**](.md)| Lorsque ce paramètre vaut &#x60;true&#x60;, le résultat de la requête contiendra, pour chaque information retournée par défaut sous forme de clé, l&#39;intitulé complet de celle-ci (vaut &#x60;false&#x60; par défaut). | [optional] 
 **query** | [**object**](.md)| Chaîne de caractères correspondant à la recherche. Ce paramètre est utilisé pour surligner en retour, dans le texte intégral de la décision, les termes correspondant avec la recherche initiale (ces termes étant délimitées par des balises &#x60;&lt;em&gt;&#x60;). | [optional] 
 **operator** | [**object**](.md)| Opérateur logique reliant les multiples termes que le paramètre &#x60;query&#x60; peut contenir (&#x60;or&#x60; par défaut, &#x60;and&#x60; ou &#x60;exact&#x60; – dans ce dernier cas le moteur recherchera exactement le contenu du paramètre &#x60;query&#x60;). | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export**
> export(batch, type=type, theme=theme, chamber=chamber, formation=formation, jurisdiction=jurisdiction, committee=committee, publication=publication, solution=solution, date_start=date_start, date_end=date_end, abridged=abridged, date_type=date_type, order=order, batch_size=batch_size, resolve_references=resolve_references, with_file_of_type=with_file_of_type)

Permet d'effectuer un export par lot de décisions de justice.

Destiné aux utilisateurs désirant procéder à leur propre indexation et mise à disposition du contenu, ce point d'entrée leur permet de récupérer des lots de décisions complètes suivant des paramètres et critères simples :  * Nature de décision (filtre) ; * Matière (filtre) ; * Chambre et formation (filtre) ; * Juridiction et commission (filtre) ; * Niveau de publication (filtre) ; * Type de solution (filtre) ; * Intervalle de dates (date de création ou de mise à jour) (filtre) ; * Date (tri) ; * Nombre de décisions par lot, index du lot (navigation).  L'export par lots est limité par défaut (pour une connexion non authentifiée) à 10 résultats par lot, pour un maximum de 1000 résultats au total.

### Example
```python
from __future__ import print_function
import time
import judilibre_client
from judilibre_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = judilibre_client.DefaultApi()
batch = NULL # object | Permet de déterminer le numéro du lot de résultats à retourner (le premier lot ayant la valeur 0).
type = NULL # object | Filtre les résultats suivant la natures des décisions (parmi les valeurs : `arret`, `qpc`, `ordonnance`, `saisie`, etc. - les valeurs disponibles sont accessibles via `GET /taxonomy?id=type`). Un export avec un paramètre `type` vide ou manquant retourne des décisions de toutes natures. (optional)
theme = NULL # object | Filtre les résultats suivant la matière (nomenclature de la Cour de cassation) relative aux décisions (les valeurs disponibles sont accessibles via `GET /taxonomy?id=theme`). Un export avec un paramètre `theme` vide ou manquant retourne des décisions relatives à toutes les matières. (optional)
chamber = NULL # object | Filtre les résultats suivant la chambre relative aux décisions (les valeurs disponibles sont accessibles via `GET /taxonomy?id=chamber`). Un export avec un paramètre `chamber` vide ou manquant retourne des décisions relatives à toutes les chambres. (optional)
formation = NULL # object | Filtre les résultats suivant la formation relative aux décisions (les valeurs disponibles sont accessibles via `GET /taxonomy?id=formation`). Un export avec un paramètre `formation` vide ou manquant retourne des décisions relatives à toutes les formations. (optional)
jurisdiction = NULL # object | Filtre les résultats suivant la juridiction relative aux décisions (les valeurs disponibles sont accessibles via `GET /taxonomy?id=jurisdiction`). Un export avec un paramètre `jurisdiction` vide ou manquant retourne des décisions relatives à toutes les juridictions. (optional)
committee = NULL # object | Filtre les résultats suivant la commission relative aux décisions (les valeurs disponibles sont accessibles via `GET /taxonomy?id=committee`). Un export avec un paramètre `committee` vide ou manquant retourne des décisions relatives à toutes les commissions. (optional)
publication = NULL # object | Filtre les résultats suivant le niveau de publication des décisions (parmi les valeurs : `b`, `r`, `l`, `c`, etc. - les valeurs disponibles sont accessibles via `GET /taxonomy?id=publication`). Un export avec un paramètre `publication` vide ou manquant retourne des décisions de n'importe quel niveau de publication. (optional)
solution = NULL # object | Filtre les résultats suivant le type de solution des décisions (parmi les valeurs : `annulation`, `avis`, `cassation`, `decheance`, `designation`, `irrecevabilite`, `nonlieu`, `qpc`, `rabat`, etc. - les valeurs disponibles sont accessibles via `GET /taxonomy?id=solution`). Un export avec un paramètre `solution` vide retourne des décisions ayant n'importe quel type de solution. (optional)
date_start = NULL # object | Combiné avec le paramètre `date_end`, permet de restreindre les résultats à un intervalle de dates, au format ISO-8601 (par exemple 2021-05-13). (optional)
date_end = NULL # object | Combiné avec le paramètre `date_start`, permet de restreindre les résultats à un intervalle de dates, au format ISO-8601 (par exemple 2021-05-13). (optional)
abridged = NULL # object | Lorsque ce paramètre vaut `true`, le résultat de la requête contiendra la version abrégée des décisions (sans texte intégral ni métadonnées détaillées, vaut `false` par défaut). (optional)
date_type = NULL # object | Type de date à prendre en compte pour l’intervalle de dates fourni pour l’export (vaut `creation` ou `update`). (optional)
order = NULL # object | Permet de choisir l’ordre du tri des décisions exportées ('asc' pour un tri par date chronologique ou 'desc' pour un tri par date antichronologique, vaut 'asc' par défaut). (optional)
batch_size = NULL # object | Permet de déterminer le nombre de résultats retournés par lot (1000 maximum, vaut 10 par défaut). (optional)
resolve_references = NULL # object | Lorsque ce paramètre vaut `true`, le résultat de la requête contiendra, pour chaque information retournée par défaut sous forme de clé, l'intitulé complet de celle-ci (vaut `false` par défaut). (optional)
with_file_of_type = NULL # object | Filtre les résultats suivant le type de documents associés aux décisions, parmi les valeurs : `prep_rapp` (Rapport du rapporteur), `prep_avis` (Avis de l’avocat général), `prep_oral` (Avis oral de l’avocat général), `comm_comm` (Communiqué), `comm_note` (Note explicative), `comm_nora` (Notice au rapport annuel), `comm_lett` (Lettre de chambre), `comm_trad` (Arrêt traduit). Les valeurs disponibles sont accessibles via `GET /taxonomy?id=filetype`. (optional)

try:
    # Permet d'effectuer un export par lot de décisions de justice.
    api_instance.export(batch, type=type, theme=theme, chamber=chamber, formation=formation, jurisdiction=jurisdiction, committee=committee, publication=publication, solution=solution, date_start=date_start, date_end=date_end, abridged=abridged, date_type=date_type, order=order, batch_size=batch_size, resolve_references=resolve_references, with_file_of_type=with_file_of_type)
except ApiException as e:
    print("Exception when calling DefaultApi->export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch** | [**object**](.md)| Permet de déterminer le numéro du lot de résultats à retourner (le premier lot ayant la valeur 0). | 
 **type** | [**object**](.md)| Filtre les résultats suivant la natures des décisions (parmi les valeurs : &#x60;arret&#x60;, &#x60;qpc&#x60;, &#x60;ordonnance&#x60;, &#x60;saisie&#x60;, etc. - les valeurs disponibles sont accessibles via &#x60;GET /taxonomy?id&#x3D;type&#x60;). Un export avec un paramètre &#x60;type&#x60; vide ou manquant retourne des décisions de toutes natures. | [optional] 
 **theme** | [**object**](.md)| Filtre les résultats suivant la matière (nomenclature de la Cour de cassation) relative aux décisions (les valeurs disponibles sont accessibles via &#x60;GET /taxonomy?id&#x3D;theme&#x60;). Un export avec un paramètre &#x60;theme&#x60; vide ou manquant retourne des décisions relatives à toutes les matières. | [optional] 
 **chamber** | [**object**](.md)| Filtre les résultats suivant la chambre relative aux décisions (les valeurs disponibles sont accessibles via &#x60;GET /taxonomy?id&#x3D;chamber&#x60;). Un export avec un paramètre &#x60;chamber&#x60; vide ou manquant retourne des décisions relatives à toutes les chambres. | [optional] 
 **formation** | [**object**](.md)| Filtre les résultats suivant la formation relative aux décisions (les valeurs disponibles sont accessibles via &#x60;GET /taxonomy?id&#x3D;formation&#x60;). Un export avec un paramètre &#x60;formation&#x60; vide ou manquant retourne des décisions relatives à toutes les formations. | [optional] 
 **jurisdiction** | [**object**](.md)| Filtre les résultats suivant la juridiction relative aux décisions (les valeurs disponibles sont accessibles via &#x60;GET /taxonomy?id&#x3D;jurisdiction&#x60;). Un export avec un paramètre &#x60;jurisdiction&#x60; vide ou manquant retourne des décisions relatives à toutes les juridictions. | [optional] 
 **committee** | [**object**](.md)| Filtre les résultats suivant la commission relative aux décisions (les valeurs disponibles sont accessibles via &#x60;GET /taxonomy?id&#x3D;committee&#x60;). Un export avec un paramètre &#x60;committee&#x60; vide ou manquant retourne des décisions relatives à toutes les commissions. | [optional] 
 **publication** | [**object**](.md)| Filtre les résultats suivant le niveau de publication des décisions (parmi les valeurs : &#x60;b&#x60;, &#x60;r&#x60;, &#x60;l&#x60;, &#x60;c&#x60;, etc. - les valeurs disponibles sont accessibles via &#x60;GET /taxonomy?id&#x3D;publication&#x60;). Un export avec un paramètre &#x60;publication&#x60; vide ou manquant retourne des décisions de n&#39;importe quel niveau de publication. | [optional] 
 **solution** | [**object**](.md)| Filtre les résultats suivant le type de solution des décisions (parmi les valeurs : &#x60;annulation&#x60;, &#x60;avis&#x60;, &#x60;cassation&#x60;, &#x60;decheance&#x60;, &#x60;designation&#x60;, &#x60;irrecevabilite&#x60;, &#x60;nonlieu&#x60;, &#x60;qpc&#x60;, &#x60;rabat&#x60;, etc. - les valeurs disponibles sont accessibles via &#x60;GET /taxonomy?id&#x3D;solution&#x60;). Un export avec un paramètre &#x60;solution&#x60; vide retourne des décisions ayant n&#39;importe quel type de solution. | [optional] 
 **date_start** | [**object**](.md)| Combiné avec le paramètre &#x60;date_end&#x60;, permet de restreindre les résultats à un intervalle de dates, au format ISO-8601 (par exemple 2021-05-13). | [optional] 
 **date_end** | [**object**](.md)| Combiné avec le paramètre &#x60;date_start&#x60;, permet de restreindre les résultats à un intervalle de dates, au format ISO-8601 (par exemple 2021-05-13). | [optional] 
 **abridged** | [**object**](.md)| Lorsque ce paramètre vaut &#x60;true&#x60;, le résultat de la requête contiendra la version abrégée des décisions (sans texte intégral ni métadonnées détaillées, vaut &#x60;false&#x60; par défaut). | [optional] 
 **date_type** | [**object**](.md)| Type de date à prendre en compte pour l’intervalle de dates fourni pour l’export (vaut &#x60;creation&#x60; ou &#x60;update&#x60;). | [optional] 
 **order** | [**object**](.md)| Permet de choisir l’ordre du tri des décisions exportées (&#39;asc&#39; pour un tri par date chronologique ou &#39;desc&#39; pour un tri par date antichronologique, vaut &#39;asc&#39; par défaut). | [optional] 
 **batch_size** | [**object**](.md)| Permet de déterminer le nombre de résultats retournés par lot (1000 maximum, vaut 10 par défaut). | [optional] 
 **resolve_references** | [**object**](.md)| Lorsque ce paramètre vaut &#x60;true&#x60;, le résultat de la requête contiendra, pour chaque information retournée par défaut sous forme de clé, l&#39;intitulé complet de celle-ci (vaut &#x60;false&#x60; par défaut). | [optional] 
 **with_file_of_type** | [**object**](.md)| Filtre les résultats suivant le type de documents associés aux décisions, parmi les valeurs : &#x60;prep_rapp&#x60; (Rapport du rapporteur), &#x60;prep_avis&#x60; (Avis de l’avocat général), &#x60;prep_oral&#x60; (Avis oral de l’avocat général), &#x60;comm_comm&#x60; (Communiqué), &#x60;comm_note&#x60; (Note explicative), &#x60;comm_nora&#x60; (Notice au rapport annuel), &#x60;comm_lett&#x60; (Lettre de chambre), &#x60;comm_trad&#x60; (Arrêt traduit). Les valeurs disponibles sont accessibles via &#x60;GET /taxonomy?id&#x3D;filetype&#x60;. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **healthcheck**
> healthcheck()

Permet de récupérer l'état de disponibilité du service.

Ce point d'entrée permet de connaître l'état de disponibilité du service (disponible ou indisponible).

### Example
```python
from __future__ import print_function
import time
import judilibre_client
from judilibre_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = judilibre_client.DefaultApi()

try:
    # Permet de récupérer l'état de disponibilité du service.
    api_instance.healthcheck()
except ApiException as e:
    print("Exception when calling DefaultApi->healthcheck: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search**
> search(query=query, field=field, operator=operator, type=type, theme=theme, chamber=chamber, formation=formation, jurisdiction=jurisdiction, committee=committee, publication=publication, solution=solution, date_start=date_start, date_end=date_end, sort=sort, order=order, page_size=page_size, page=page, resolve_references=resolve_references, with_file_of_type=with_file_of_type)

Permet d'effectuer une recherche dans les données ouvertes des décisions de justice.

Le point d'entrée `GET /search` permet d'effectuer une recherche dans la base de données ouverte des décisions de justice, suivant les paramètres, filtres et critères suivants :  * Texte en saisie libre, lequel sera mis en correspondance avec tout ou partie du contenu des décisions ; * Le mode de mise en rapport des termes de la recherche (*ou*, *et*, expression exacte) ; * Contenu ciblé par la recherche : décision intégrale, zones spécifiques de la décision (exposé du litige, moyens, motivations, dispositif), sommaire, titrages, numéro de pourvoi, etc. ; * Nature de décision (filtre) ; * Matière (filtre) ; * Chambre et formation (filtre) ; * Juridiction et commission (filtre) ; * Niveau de publication (filtre) ; * Type de solution (filtre) ; * Intervalle de dates (filtre) ; * Pertinence et date (tri) ; * Nombre de résultats par page et index de la page de résultats affichée (navigation).  La pertinence de la recherche équivaut à un score calculé par Elasticsearch à partir de la correspondance entre le texte en saisie libre et le contenu recherché. Par défaut, le moteur de recherche retourne les résultats classés par pertinence décroissante.  Les filtres sélectionnés ne modifient pas le score, mais permettent de retirer des résultats les décisions dont le contenu ne coïncide pas avec eux.  Le résultat de la recherche est nécessairement paginé (avec un maximum de 50 résultats par page, pour un maximum de 10 000 résultats au total) et ne contient qu'un aperçu des décisions trouvées (chacune possédant un identifiant unique).  Certaines des informations ne sont retournées que sous forme de clé ou d'identifiant numérique (juridiction, chambre, niveau de publication, etc.). Il convient dès lors d'utiliser le point d'entrée `GET /taxonomy` pour en récupérer l'intitulé complet, ou d'effectuer la requête en utilisant le paramètre `resolve_references=true`.  Le texte intégral et les zones qu'il contient ne sont pas inclus dans les résultats de la recherche.  La récupération d'une décision complète (incluant son texte et les zones qu'il contient) repose sur le point d'entrée `GET /decision`.

### Example
```python
from __future__ import print_function
import time
import judilibre_client
from judilibre_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = judilibre_client.DefaultApi()
query = NULL # object | Chaîne de caractères correspondant à la recherche. Une recherche avec un paramètre `query` vide ou manquant est ignorée et retourne un résultat vide. (optional)
field = NULL # object | Liste des champs, métadonnées ou zones de contenu ciblés par la recherche (parmi les valeurs : `expose`, `moyens`, `motivations`, `dispositif`, `annexes`, `sommaire`, `titrage`, etc. - les valeurs disponibles sont accessibles via `GET /taxonomy?id=field`). Une recherche avec un paramètre `field` vide ou manquant est appliquée à l'intégralité de la décision (introduction et moyens annexés compris) mais va exclure les métadonnées (sommaire, titrage, etc.). (optional)
operator = NULL # object | Opérateur logique reliant les multiples termes que le paramètre `query` peut contenir (`or` par défaut, `and` ou `exact` – dans ce dernier cas le moteur recherchera exactement le contenu du paramètre `query`). (optional)
type = NULL # object | Filtre les résultats suivant la natures des décisions (parmi les valeurs : `arret`, `qpc`, `ordonnance`, `saisie`, etc. - les valeurs disponibles sont accessibles via `GET /taxonomy?id=type`). Une recherche avec un paramètre `type` vide ou manquant retourne des décisions de toutes natures. (optional)
theme = NULL # object | Filtre les résultats suivant la matière (nomenclature de la Cour de cassation) relative aux décisions (les valeurs disponibles sont accessibles via `GET /taxonomy?id=theme`). Une recherche avec un paramètre `theme` vide ou manquant retourne des décisions relatives à toutes les matières. (optional)
chamber = NULL # object | Filtre les résultats suivant la chambre relative aux décisions (les valeurs disponibles sont accessibles via `GET /taxonomy?id=chamber`). Une recherche avec un paramètre `chamber` vide ou manquant retourne des décisions relatives à toutes les chambres. (optional)
formation = NULL # object | Filtre les résultats suivant la formation relative aux décisions (les valeurs disponibles sont accessibles via `GET /taxonomy?id=formation`). Une recherche avec un paramètre `formation` vide ou manquant retourne des décisions relatives à toutes les formations. (optional)
jurisdiction = NULL # object | Filtre les résultats suivant la juridiction relative aux décisions (les valeurs disponibles sont accessibles via `GET /taxonomy?id=jurisdiction`). Une recherche avec un paramètre `jurisdiction` vide ou manquant retourne des décisions relatives à toutes les juridictions. (optional)
committee = NULL # object | Filtre les résultats suivant la commission relative aux décisions (les valeurs disponibles sont accessibles via `GET /taxonomy?id=committee`). Une recherche avec un paramètre `committee` vide ou manquant retourne des décisions relatives à toutes les commissions. (optional)
publication = NULL # object | Filtre les résultats suivant le niveau de publication des décisions (parmi les valeurs : `b`, `r`, `l`, `c`, etc. - les valeurs disponibles sont accessibles via `GET /taxonomy?id=publication`). Une recherche avec un paramètre `publication` vide ou manquant retourne des décisions de n'importe quel niveau de publication. (optional)
solution = NULL # object | Filtre les résultats suivant le type de solution des décisions (parmi les valeurs : `annulation`, `avis`, `cassation`, `decheance`, `designation`, `irrecevabilite`, `nonlieu`, `qpc`, `rabat`, etc. - les valeurs disponibles sont accessibles via `GET /taxonomy?id=solution`). Une recherche avec un paramètre `solution` vide retourne des décisions ayant n'importe quel type de solution. (optional)
date_start = NULL # object | Combiné avec le paramètre `date_end`, permet de restreindre les résultats à un intervalle de dates, au format ISO-8601 (par exemple 2021-05-13). (optional)
date_end = NULL # object | Combiné avec le paramètre `date_start`, permet de restreindre les résultats à un intervalle de dates, au format ISO-8601 (par exemple 2021-05-13). (optional)
sort = NULL # object | Permet de choisir la valeur suivant laquelle les résultats sont triés (`score` pour un tri par pertinence, `scorepub` pour un tri par pertinence et niveau de publication et `date` pour un tri par date, vaut `scorepub` par défaut). (optional)
order = NULL # object | Permet de choisir l'ordre du tri (`asc` pour un tri ascendant ou `desc` pour un tri descendant, vaut `desc` par défaut). (optional)
page_size = NULL # object | Permet de déterminer le nombre de résultats retournés par page (50 maximum, vaut 10 par défaut). (optional)
page = NULL # object | Permet de déterminer le numéro de la page de résultats à retourner (la première page valant `0`). (optional)
resolve_references = NULL # object | Lorsque ce paramètre vaut `true`, le résultat de la requête contiendra, pour chaque information retournée par défaut sous forme de clé, l'intitulé complet de celle-ci (vaut `false` par défaut). (optional)
with_file_of_type = NULL # object | Filtre les résultats suivant le type de documents associés aux décisions, parmi les valeurs : `prep_rapp` (Rapport du rapporteur), `prep_avis` (Avis de l’avocat général), `prep_oral` (Avis oral de l’avocat général), `comm_comm` (Communiqué), `comm_note` (Note explicative), `comm_nora` (Notice au rapport annuel), `comm_lett` (Lettre de chambre), `comm_trad` (Arrêt traduit). Les valeurs disponibles sont accessibles via `GET /taxonomy?id=filetype`. (optional)

try:
    # Permet d'effectuer une recherche dans les données ouvertes des décisions de justice.
    api_instance.search(query=query, field=field, operator=operator, type=type, theme=theme, chamber=chamber, formation=formation, jurisdiction=jurisdiction, committee=committee, publication=publication, solution=solution, date_start=date_start, date_end=date_end, sort=sort, order=order, page_size=page_size, page=page, resolve_references=resolve_references, with_file_of_type=with_file_of_type)
except ApiException as e:
    print("Exception when calling DefaultApi->search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**object**](.md)| Chaîne de caractères correspondant à la recherche. Une recherche avec un paramètre &#x60;query&#x60; vide ou manquant est ignorée et retourne un résultat vide. | [optional] 
 **field** | [**object**](.md)| Liste des champs, métadonnées ou zones de contenu ciblés par la recherche (parmi les valeurs : &#x60;expose&#x60;, &#x60;moyens&#x60;, &#x60;motivations&#x60;, &#x60;dispositif&#x60;, &#x60;annexes&#x60;, &#x60;sommaire&#x60;, &#x60;titrage&#x60;, etc. - les valeurs disponibles sont accessibles via &#x60;GET /taxonomy?id&#x3D;field&#x60;). Une recherche avec un paramètre &#x60;field&#x60; vide ou manquant est appliquée à l&#39;intégralité de la décision (introduction et moyens annexés compris) mais va exclure les métadonnées (sommaire, titrage, etc.). | [optional] 
 **operator** | [**object**](.md)| Opérateur logique reliant les multiples termes que le paramètre &#x60;query&#x60; peut contenir (&#x60;or&#x60; par défaut, &#x60;and&#x60; ou &#x60;exact&#x60; – dans ce dernier cas le moteur recherchera exactement le contenu du paramètre &#x60;query&#x60;). | [optional] 
 **type** | [**object**](.md)| Filtre les résultats suivant la natures des décisions (parmi les valeurs : &#x60;arret&#x60;, &#x60;qpc&#x60;, &#x60;ordonnance&#x60;, &#x60;saisie&#x60;, etc. - les valeurs disponibles sont accessibles via &#x60;GET /taxonomy?id&#x3D;type&#x60;). Une recherche avec un paramètre &#x60;type&#x60; vide ou manquant retourne des décisions de toutes natures. | [optional] 
 **theme** | [**object**](.md)| Filtre les résultats suivant la matière (nomenclature de la Cour de cassation) relative aux décisions (les valeurs disponibles sont accessibles via &#x60;GET /taxonomy?id&#x3D;theme&#x60;). Une recherche avec un paramètre &#x60;theme&#x60; vide ou manquant retourne des décisions relatives à toutes les matières. | [optional] 
 **chamber** | [**object**](.md)| Filtre les résultats suivant la chambre relative aux décisions (les valeurs disponibles sont accessibles via &#x60;GET /taxonomy?id&#x3D;chamber&#x60;). Une recherche avec un paramètre &#x60;chamber&#x60; vide ou manquant retourne des décisions relatives à toutes les chambres. | [optional] 
 **formation** | [**object**](.md)| Filtre les résultats suivant la formation relative aux décisions (les valeurs disponibles sont accessibles via &#x60;GET /taxonomy?id&#x3D;formation&#x60;). Une recherche avec un paramètre &#x60;formation&#x60; vide ou manquant retourne des décisions relatives à toutes les formations. | [optional] 
 **jurisdiction** | [**object**](.md)| Filtre les résultats suivant la juridiction relative aux décisions (les valeurs disponibles sont accessibles via &#x60;GET /taxonomy?id&#x3D;jurisdiction&#x60;). Une recherche avec un paramètre &#x60;jurisdiction&#x60; vide ou manquant retourne des décisions relatives à toutes les juridictions. | [optional] 
 **committee** | [**object**](.md)| Filtre les résultats suivant la commission relative aux décisions (les valeurs disponibles sont accessibles via &#x60;GET /taxonomy?id&#x3D;committee&#x60;). Une recherche avec un paramètre &#x60;committee&#x60; vide ou manquant retourne des décisions relatives à toutes les commissions. | [optional] 
 **publication** | [**object**](.md)| Filtre les résultats suivant le niveau de publication des décisions (parmi les valeurs : &#x60;b&#x60;, &#x60;r&#x60;, &#x60;l&#x60;, &#x60;c&#x60;, etc. - les valeurs disponibles sont accessibles via &#x60;GET /taxonomy?id&#x3D;publication&#x60;). Une recherche avec un paramètre &#x60;publication&#x60; vide ou manquant retourne des décisions de n&#39;importe quel niveau de publication. | [optional] 
 **solution** | [**object**](.md)| Filtre les résultats suivant le type de solution des décisions (parmi les valeurs : &#x60;annulation&#x60;, &#x60;avis&#x60;, &#x60;cassation&#x60;, &#x60;decheance&#x60;, &#x60;designation&#x60;, &#x60;irrecevabilite&#x60;, &#x60;nonlieu&#x60;, &#x60;qpc&#x60;, &#x60;rabat&#x60;, etc. - les valeurs disponibles sont accessibles via &#x60;GET /taxonomy?id&#x3D;solution&#x60;). Une recherche avec un paramètre &#x60;solution&#x60; vide retourne des décisions ayant n&#39;importe quel type de solution. | [optional] 
 **date_start** | [**object**](.md)| Combiné avec le paramètre &#x60;date_end&#x60;, permet de restreindre les résultats à un intervalle de dates, au format ISO-8601 (par exemple 2021-05-13). | [optional] 
 **date_end** | [**object**](.md)| Combiné avec le paramètre &#x60;date_start&#x60;, permet de restreindre les résultats à un intervalle de dates, au format ISO-8601 (par exemple 2021-05-13). | [optional] 
 **sort** | [**object**](.md)| Permet de choisir la valeur suivant laquelle les résultats sont triés (&#x60;score&#x60; pour un tri par pertinence, &#x60;scorepub&#x60; pour un tri par pertinence et niveau de publication et &#x60;date&#x60; pour un tri par date, vaut &#x60;scorepub&#x60; par défaut). | [optional] 
 **order** | [**object**](.md)| Permet de choisir l&#39;ordre du tri (&#x60;asc&#x60; pour un tri ascendant ou &#x60;desc&#x60; pour un tri descendant, vaut &#x60;desc&#x60; par défaut). | [optional] 
 **page_size** | [**object**](.md)| Permet de déterminer le nombre de résultats retournés par page (50 maximum, vaut 10 par défaut). | [optional] 
 **page** | [**object**](.md)| Permet de déterminer le numéro de la page de résultats à retourner (la première page valant &#x60;0&#x60;). | [optional] 
 **resolve_references** | [**object**](.md)| Lorsque ce paramètre vaut &#x60;true&#x60;, le résultat de la requête contiendra, pour chaque information retournée par défaut sous forme de clé, l&#39;intitulé complet de celle-ci (vaut &#x60;false&#x60; par défaut). | [optional] 
 **with_file_of_type** | [**object**](.md)| Filtre les résultats suivant le type de documents associés aux décisions, parmi les valeurs : &#x60;prep_rapp&#x60; (Rapport du rapporteur), &#x60;prep_avis&#x60; (Avis de l’avocat général), &#x60;prep_oral&#x60; (Avis oral de l’avocat général), &#x60;comm_comm&#x60; (Communiqué), &#x60;comm_note&#x60; (Note explicative), &#x60;comm_nora&#x60; (Notice au rapport annuel), &#x60;comm_lett&#x60; (Lettre de chambre), &#x60;comm_trad&#x60; (Arrêt traduit). Les valeurs disponibles sont accessibles via &#x60;GET /taxonomy?id&#x3D;filetype&#x60;. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stats**
> stats()

Permet de récupérer des statistiques sur le contenu de la base JUDILIBRE.

Ce point d'entrée publiera notamment les statistiques suivantes, mises à jour quotidiennement :  * Nombre de décisions indexées (au total, par année, par juridiction) ; * Nombre de requêtes (par jour, par semaine, etc.) ; * Date de la décision la plus ancienne, date de la décision la plus récente.

### Example
```python
from __future__ import print_function
import time
import judilibre_client
from judilibre_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = judilibre_client.DefaultApi()

try:
    # Permet de récupérer des statistiques sur le contenu de la base JUDILIBRE.
    api_instance.stats()
except ApiException as e:
    print("Exception when calling DefaultApi->stats: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **taxonomy**
> taxonomy(id=id, key=key, value=value, context_value=context_value)

Permet de récupérer les listes des termes employés par le processus de recherche.

L'API publique propose la récupération des listes des termes (sous la forme d'un couple clé/valeur) constituants les différents critères et filtres pris en compte par le processus de recherche et les données qu'il restitue, notamment :  * La liste des types de décision (`type`) ; * La liste des juridictions dont le système intègre les décisions (`jurisdiction`) ; * La liste des chambres (`chamber`) ; * La liste des formations (`formation`) ; * La liste des commissions (`committee`) ; * La liste des niveaux de publication (`publication`) ; * La liste des matières (`theme`) ; * La liste des solutions (`solution`) ; * La liste des champs et des zones de contenu des décisions pouvant être ciblés par la recherche (`field`) ; * La liste des zones de contenu des décisions (`zones`) ; * etc.  La publication de cette taxonomie permet principalement au prestataire chargé de l'implémentation du frontend (ainsi qu'à certains réutilisateurs avancés) d'automatiser la constitution des formulaires de recherche et l'enrichissement des résultats retournés.

### Example
```python
from __future__ import print_function
import time
import judilibre_client
from judilibre_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = judilibre_client.DefaultApi()
id = NULL # object | Identifiant de l'entrée de taxonomie à interroger (`type`, `jurisdiction`, `chamber`, etc. - les valeurs disponibles sont accessibles via `GET /taxonomy` sans paramètre). (optional)
key = NULL # object | Clé du terme dont on veut récupérer l'intitulé complet (le paramètre `id` est alors requis), par exemple : la requête `GET /taxonomy?id=jurisdiction&key=cc` retournera `Cour de cassation`. (optional)
value = NULL # object | Intitulé complet du terme dont on veut récupérer la clé (le paramètre `id` est alors requis), par exemple : la requête `GET /taxonomy?id=jurisdiction&value=cour%20de%20cassation` retournera `cc`. (optional)
context_value = NULL # object | Valeur pouvant être requise pour contextualiser certaines listes (par exemple, la liste des chambres qui n’a de sens que dans le contexte d’une juridiction – ainsi, pour obtenir la liste des chambres de la Cour de cassation : `GET /taxonomy?id=chamber&context_value=cc`). (optional)

try:
    # Permet de récupérer les listes des termes employés par le processus de recherche.
    api_instance.taxonomy(id=id, key=key, value=value, context_value=context_value)
except ApiException as e:
    print("Exception when calling DefaultApi->taxonomy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| Identifiant de l&#39;entrée de taxonomie à interroger (&#x60;type&#x60;, &#x60;jurisdiction&#x60;, &#x60;chamber&#x60;, etc. - les valeurs disponibles sont accessibles via &#x60;GET /taxonomy&#x60; sans paramètre). | [optional] 
 **key** | [**object**](.md)| Clé du terme dont on veut récupérer l&#39;intitulé complet (le paramètre &#x60;id&#x60; est alors requis), par exemple : la requête &#x60;GET /taxonomy?id&#x3D;jurisdiction&amp;key&#x3D;cc&#x60; retournera &#x60;Cour de cassation&#x60;. | [optional] 
 **value** | [**object**](.md)| Intitulé complet du terme dont on veut récupérer la clé (le paramètre &#x60;id&#x60; est alors requis), par exemple : la requête &#x60;GET /taxonomy?id&#x3D;jurisdiction&amp;value&#x3D;cour%20de%20cassation&#x60; retournera &#x60;cc&#x60;. | [optional] 
 **context_value** | [**object**](.md)| Valeur pouvant être requise pour contextualiser certaines listes (par exemple, la liste des chambres qui n’a de sens que dans le contexte d’une juridiction – ainsi, pour obtenir la liste des chambres de la Cour de cassation : &#x60;GET /taxonomy?id&#x3D;chamber&amp;context_value&#x3D;cc&#x60;). | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

