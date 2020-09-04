=============
Page Template
=============

Im Page Template ``src/vs.registration/vs/registration/browser/registration.pt`` wird nun ein Formular mit der ID ``confirm-registrant`` und den entsprechenden ``input``-Feldern eingetragen::

 <tal:registrants condition="view/have_registrants">
     <h2 i18n:translate="title_registration_contents">Registrants</h2>
     <form action="confirmRegistrant">
         <tal:block repeat="registrant view/registrants">
             <dt>
                 <a tal:attributes="href registrant/url"
                    tal:content="registrant/title" />
             </dt>
             <dd tal:content="registrant/address" />
             <dd>
                 <input class="kssattr-confirm-yes"
                        type="submit"
                        name="vs.registration.confirm.confirm"
                        value="yes"
                        i18n:attributes="value"
                        i18n:attributes="confirm-button"
                        />
                 <input class="kssattr-confirm-no"
                        type="submit"
                        name="vs.registration.confirm.reject"
                        value="no"
                        i18n:attributes="value"
                        i18n:attributes="reject-button"
                        />
             </dd>
         </tal:block>
     </form>
 </tal:registrants>
