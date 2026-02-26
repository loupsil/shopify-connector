/** @odoo-module **/

import { Component } from "@odoo/owl";
import { registry } from "@web/core/registry";

class ShopifyConnectorAction extends Component {
    static template = "shopify_connector_dasolo.ShopifyConnectorAction";

    setup() {
        this.iframeSrc = "https://odoo-shopify-connector.dasolo.ai/login";
    }
}

registry.category("actions").add("shopify_connector_dasolo_action", ShopifyConnectorAction);
