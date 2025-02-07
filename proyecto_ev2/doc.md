# PROYECTO 2A EVALUACIÓN: AMPLIACIÓN MÓDULO SUSCRIPCIONES MEDIANTE MÉTRICAS Y ESTADÍSTICAS

## MÓDULO MÉTRICAS:

```
# -*- coding: utf-8 -*-
from odoo import models, fields, api  # type: ignore

class SubscriptionMetrics(models.Model):
    _name = 'subscription.subscription_metrics'
    _description = 'Métricas de Suscripciones'

    # 1. Fecha
    date = fields.Date(
        string="Fecha",
        default=fields.Date.today
    )
    # 2. Número de suscripciones activas
    active_subscriptions = fields.Integer(
        string="Número de Suscripciones Activas"
    )
    # 3. Ingresos generados
    generated_revenue = fields.Float(
        string="Ingresos Generados",
        digits=(12, 2)
    )
    # 4. Tasa de renovación
    renewal_rate = fields.Float(
        string="Tasa de Renovación",
        compute="_compute_rates",
        digits=(12, 2),
        help="(Renovaciones / Suscripciones Activas) * 100"
    )
    # 5. Tasa de cancelación
    cancellation_rate = fields.Float(
        string="Tasa de Cancelación",
        compute="_compute_rates",
        digits=(12, 2),
        help="(Cancelaciones / Suscripciones Activas) * 100"
    )
    # 6. Renovaciones
    renewals = fields.Integer(
        string="Renovaciones"
    )
    # 7. Nuevas suscripciones
    new_subscriptions = fields.Integer(
        string="Nuevas Suscripciones"
    )
    # 8. Suscripciones canceladas
    cancelled_subscriptions = fields.Integer(
        string="Suscripciones Canceladas"
    )
    # 9. Clientes recurrentes y Nuevos clientes
    recurring_customers = fields.Integer(
        string="Clientes Recurrentes"
    )
    new_customers = fields.Integer(
        string="Nuevos Clientes"
    )
    # 10. Ingresos promedio por usuario
    arpu = fields.Float(
        string="Ingresos Promedio por Usuario (ARPU)",
        compute="_compute_arpu",
        digits=(12, 2)
    )
    # 11. Tasa de conversión
    conversion_rate = fields.Float(
        string="Tasa de Conversión"
    )
    # 12. Churn Rate
    churn_rate = fields.Float(
        string="Churn Rate (Tasa de Pérdida de Clientes)"
    )
    # 13. Lifetime Value (LTV)
    ltv = fields.Float(
        string="Lifetime Value (LTV)",
        digits=(12, 2)
    )
    # 14. Costo de adquisición de clientes
    cac = fields.Float(
        string="Costo de Adquisición de Clientes (CAC)",
        digits=(12, 2)
    )
    # 15. Notas
    notes = fields.Text(
        string="Notas"
    )
    # 16. Relación con el Modelo de Suscripciones
    subscription_ids = fields.One2many(
        comodel_name='subscription.subscription',
        inverse_name='metric_id',
        string="Suscripciones Relacionadas"
    )

    @api.depends('active_subscriptions', 'renewals', 'cancelled_subscriptions')
    def _compute_rates(self):
        for rec in self:
            if rec.active_subscriptions:
                rec.renewal_rate = (rec.renewals / rec.active_subscriptions) * 100
                rec.cancellation_rate = (rec.cancelled_subscriptions / rec.active_subscriptions) * 100
            else:
                rec.renewal_rate = 0.0
                rec.cancellation_rate = 0.0

    @api.depends('active_subscriptions', 'generated_revenue')
    def _compute_arpu(self):
        for rec in self:
            if rec.active_subscriptions:
                rec.arpu = rec.generated_revenue / rec.active_subscriptions
            else:
                rec.arpu = 0.0
```

## Vista:

```
<odoo>
    <data>
        <!-- Vista de lista básica -->
        <record model="ir.ui.view" id="view_subscription_tree_basic">
            <field name="name">subscription.tree.basic</field>
            <field name="model">subscription.subscription</field>
            <field name="arch" type="xml">
                <tree string="Suscripciones (Básico)" limit="15"
                      decoration-danger="status == 'expired'"
                      decoration-warning="status == 'cancelled'">
                    <field name="name" string="Nombre"/>
                    <field name="customer_id" string="Cliente"/>
                    <field name="subscription_code" string="Código"/>
                    <field name="start_date" string="Inicio"/>
                    <field name="end_date" string="Fin" widget="remaining_days"/>
                    <field name="duration_months" string="Duración (meses)"/>
                    <field name="renewal_date" string="Renovación"/>
                    <field name="status" string="Estado"/>
                    <field name="is_renewable" string="Renovable"/>
                    <field name="auto_renewal" string="Renovación Automática"/>
                    <field name="price" string="Precio" attrs="{'invisible': [('status', '=', 'cancelled')]}"/>
                    <button name="action_add_15_days" string="Añadir 15 Días" type="object" class="btn-primary"/>
                </tree>
            </field>
        </record>

        <!-- Vista de lista de uso -->
        <record id="view_subscription_tree_usage" model="ir.ui.view">
            <field name="name">subscription.tree.usage</field>
            <field name="model">subscription.subscription</field>
            <field name="arch" type="xml">
                <tree string="Suscripciones (Uso)" limit="15">
                    <field name="name" string="Nombre"/>
                    <field name="usage_limit" string="Límite de Uso"/>
                    <field name="current_usage" string="Uso Actual"/>
                    <field name="use_percent" string="Porcentaje de Uso" decoration-danger="use_percent > 80" avg="1"
                           widget="progressbar"/>
                </tree>
            </field>
        </record>

        <!-- Vista de lista para Métricas -->
        <record id="view_subscription_metrics_tree" model="ir.ui.view">
            <field name="name">subscription.metrics.tree</field>
            <field name="model">subscription.subscription_metrics</field>
            <field name="arch" type="xml">
                <tree string="Métricas de Suscripciones">
                    <field name="date"/>
                    <field name="active_subscriptions"/>
                    <field name="generated_revenue"/>
                    <field name="renewal_rate"/>
                    <field name="cancellation_rate"/>
                    <field name="arpu"/>
                </tree>
            </field>
        </record>

        <!-- Vista formulario -->
        <record id="view_subscription_form_custom" model="ir.ui.view">
            <field name="name">subscription.subscription.form.custom</field>
            <field name="model">subscription.subscription</field>
            <field name="arch" type="xml">
                <form string="Suscripción">
                    <sheet>
                        <group>
                            <field name="name" placeholder="Nombre de la Suscripción"/>
                            <field name="customer_id"/>
                            <field name="subscription_code"/>
                        </group>

                        <notebook>
                            <page string="Datos Básicos">
                                <group>
                                    <field name="start_date"/>
                                    <field name="end_date" widget="remaining_days"/>
                                    <field name="duration_months"/>
                                    <field name="renewal_date"/>
                                    <field name="status"/>
                                    <field name="is_renewable"/>
                                    <field name="auto_renewal"/>
                                    <field name="price" attrs="{'invisible': [('status', '=', 'cancelled')]}"/>
                                </group>
                            </page>

                            <page string="Datos de Uso">
                                <group>
                                    <field name="usage_limit"/>
                                    <field name="current_usage"/>
                                    <field name="use_percent"/>
                                </group>
                            </page>
                        </notebook>
                    </sheet>
                </form>
            </field>
        </record>

        <!-- Vista de formulario para Métricas -->
        <record id="view_subscription_metrics_form" model="ir.ui.view">
            <field name="name">subscription.metrics.form</field>
            <field name="model">subscription.subscription_metrics</field>
            <field name="arch" type="xml">
                <form string="Detalle de Métricas">
                    <sheet>
                        <group>
                            <field name="date"/>
                            <field name="active_subscriptions"/>
                            <field name="generated_revenue"/>
                        </group>
                        <group>
                            <field name="renewals"/>
                            <field name="new_subscriptions"/>
                            <field name="cancelled_subscriptions"/>
                        </group>
                        <group>
                            <field name="renewal_rate"/>
                            <field name="cancellation_rate"/>
                            <field name="arpu"/>
                        </group>
                        <group>
                            <field name="recurring_customers"/>
                            <field name="new_customers"/>
                        </group>
                        <group>
                            <field name="conversion_rate"/>
                            <field name="churn_rate"/>
                            <field name="ltv"/>
                            <field name="cac"/>
                        </group>
                        <notebook>
                            <page string="Notas">
                                <field name="notes"/>
                            </page>
                            <page string="Suscripciones Relacionadas">
                                El contexto vacío impide que se hereden campos que no concuerden y evitar errores
                                <field name="subscription_ids" context="{}"/>
                            </page>
                        </notebook>
                    </sheet>
                </form>
            </field>
        </record>


        <!-- actions opening views on models -->
        <record id="action_subscription_basic" model="ir.actions.act_window">
            <field name="name">Suscripciones (Básico)</field>
            <field name="res_model">subscription.subscription</field>
            <field name="view_mode">tree,form</field>
            <field name="view_id" ref="view_subscription_tree_basic"/>
            <field name="views" eval="[
                (ref('view_subscription_tree_basic'), 'tree'),
                (ref('view_subscription_form_custom'), 'form')
            ]"/>
        </record>

        <record id="action_subscription_usage" model="ir.actions.act_window">
            <field name="name">Suscripciones (Uso)</field>
            <field name="res_model">subscription.subscription</field>
            <field name="view_mode">tree,form</field>
            <field name="view_id" ref="view_subscription_tree_usage"/>
            <field name="views" eval="[
                (ref('view_subscription_tree_usage'), 'tree'),
                (ref('view_subscription_form_custom'), 'form')
            ]"/>
        </record>

        <record id="action_subscription_metrics" model="ir.actions.act_window">
            <field name="name">Métricas de Suscripciones</field>
            <field name="res_model">subscription.subscription_metrics</field>
            <field name="view_mode">tree,form</field>
            <field name="view_id" ref="view_subscription_metrics_tree"/>
            <field name="views" eval="[
                (ref('view_subscription_metrics_tree'), 'tree'),
                (ref('view_subscription_metrics_form'), 'form')
            ]"/>
        </record>

        <!-- Top menu item -->
        <menuitem id="menu_subscription_root" name="Suscripciones"/>
        <menuitem id="menu_subscription_basic" parent="menu_subscription_root" action="action_subscription_basic"/>
        <menuitem id="menu_subscription_usage" parent="menu_subscription_root" action="action_subscription_usage"/>
        <menuitem id="menu_subscription_metrics" parent="menu_subscription_root" action="action_subscription_metrics"/>
    </data>
</odoo>
```

## MANIFEST:

```
# -*- coding: utf-8 -*-
{
    'name': "subscription",

    'summary': """
    Gestionar Suscripciones""",

    'description': """
        Gestionar Suscripciones
    """,

    'author': "Javier",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/welcome_message_web.xml',
        'views/subscription_list_web.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
```

## SECURITY:

```
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_subscription_subscription,subscription.subscription,model_subscription_subscription,base.group_user,1,1,1,1
access_subscription_subscription_metrics,subscription.subscription_metrics,model_subscription_subscription_metrics,base.group_user,1,1,1,1
```